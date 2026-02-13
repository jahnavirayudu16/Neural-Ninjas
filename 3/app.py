from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
import os
from datetime import datetime
try:
    import google.generativeai as genai
except Exception as _genai_import_error:
    genai = None
    print("⚠️  Warning: google.generativeai not available or incompatible:", _genai_import_error)

# Import mock AI fallback
from mock_ai import get_mock_recommendation, get_mock_trends, get_mock_image_analysis, get_mock_chat_response
from werkzeug.utils import secure_filename
import base64

load_dotenv()

CWD = os.path.abspath(os.path.dirname(__file__))
FRONTEND_DIR = os.path.abspath(os.path.join(CWD, '..', 'frontend'))

# Create Flask app (we'll serve frontend static files from `frontend/`)
app = Flask(__name__, static_folder=None)
CORS(app)

# Configuration
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL', 'sqlite:///stylesense.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16MB max file size
UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

db = SQLAlchemy(app)

# Initialize Gemini API
gemini_api_key = os.getenv('GEMINI_API_KEY')
if genai is not None:
    if gemini_api_key:
        genai.configure(api_key=gemini_api_key)
    else:
        print("⚠️  Warning: GEMINI_API_KEY not found in .env file")
else:
    print("⚠️  Info: Gemini AI client disabled — AI endpoints will return 503 until compatible packages are installed or a supported Python version is used.")

# Default model names (can be overridden via .env)
GEMINI_MODEL = os.getenv('GEMINI_MODEL', 'models/gemini-pro-latest')
GEMINI_VISION_MODEL = os.getenv('GEMINI_VISION_MODEL', 'models/gemini-2.5-flash')

# Models
class UserPreference(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.String(100), unique=True, nullable=False)
    occasion = db.Column(db.String(50), nullable=False)
    gender = db.Column(db.String(20), nullable=False)
    favorite_colors = db.Column(db.String(255), nullable=False)
    budget = db.Column(db.String(50), nullable=False)
    style_type = db.Column(db.String(50), nullable=False)
    body_type = db.Column(db.String(50), nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

class SavedOutfit(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.String(100), nullable=False)
    outfit_description = db.Column(db.Text, nullable=False)
    accessories = db.Column(db.Text, nullable=True)
    styling_tips = db.Column(db.Text, nullable=True)
    occasion = db.Column(db.String(50), nullable=False)
    rating = db.Column(db.Integer, default=0)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

class OutfitAnalysis(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.String(100), nullable=False)
    image_name = db.Column(db.String(255), nullable=False)
    analysis_result = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

# Routes
@app.route('/', methods=['GET'])
def home():
    # Serve frontend index if available, otherwise health JSON
    index_path = os.path.join(FRONTEND_DIR, 'index.html')
    if os.path.exists(index_path):
        return send_from_directory(FRONTEND_DIR, 'index.html')
    return jsonify({'message': 'StyleSense AI Fashion Recommender - API Server Running ✨'}), 200


# Serve frontend static files (CSS/JS/HTML/assets)
@app.route('/<path:path>', methods=['GET'])
def serve_frontend(path):
    # Let API routes be handled by Flask first
    if path.startswith('api/') or path.startswith('api'):
        return jsonify({'error': 'Not found'}), 404
    target = os.path.join(FRONTEND_DIR, path)
    if os.path.exists(target):
        return send_from_directory(FRONTEND_DIR, path)
    # fallback to index for client-side routing
    index_path = os.path.join(FRONTEND_DIR, 'index.html')
    if os.path.exists(index_path):
        return send_from_directory(FRONTEND_DIR, 'index.html')
    return jsonify({'error': 'Not found'}), 404

@app.route('/api/preferences', methods=['POST'])
def save_preferences():
    """Save user preferences"""
    try:
        data = request.json
        user_id = data.get('user_id', 'guest')
        
        preference = UserPreference.query.filter_by(user_id=user_id).first()
        
        if preference:
            preference.occasion = data.get('occasion')
            preference.gender = data.get('gender')
            preference.favorite_colors = data.get('favorite_colors')
            preference.budget = data.get('budget')
            preference.style_type = data.get('style_type')
            preference.body_type = data.get('body_type')
            preference.updated_at = datetime.utcnow()
        else:
            preference = UserPreference(
                user_id=user_id,
                occasion=data.get('occasion'),
                gender=data.get('gender'),
                favorite_colors=data.get('favorite_colors'),
                budget=data.get('budget'),
                style_type=data.get('style_type'),
                body_type=data.get('body_type')
            )
        
        db.session.add(preference)
        db.session.commit()
        
        return jsonify({'success': True, 'message': 'Preferences saved'}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

@app.route('/api/recommendations', methods=['POST'])
def get_recommendations():
    """Get AI outfit recommendations based on preferences"""
    try:
        data = request.json
        
        # Try real Gemini first, then fallback to mock
        if genai is not None:
            try:
                prompt = f"""You are a professional AI fashion stylist. Based on the following user preferences, 
                suggest a complete outfit with styling tips.

                User Details:
                - Occasion: {data.get('occasion')}
                - Gender: {data.get('gender')}
                - Favorite Colors: {data.get('favorite_colors')}
                - Budget: {data.get('budget')}
                - Style Type: {data.get('style_type')}
                - Body Type: {data.get('body_type', 'Not specified')}

                Please provide:
                1. Complete outfit suggestion
                2. Footwear recommendation
                3. Accessories suggestions
                4. Hairstyle ideas
                5. Styling tips
                6. Color coordination advice

                Format your response clearly with sections."""
                
                model = genai.GenerativeModel(GEMINI_MODEL)
                response = model.generate_content(prompt)
                
                return jsonify({
                    'success': True,
                    'recommendation': response.text,
                    'occasion': data.get('occasion')
                }), 200
            except Exception as gemini_error:
                # Fall through to mock if Gemini fails
                print(f"⚠️  Gemini API error: {gemini_error}, using mock AI")
        
        # Use mock AI as fallback
        recommendation = get_mock_recommendation(
            occasion=data.get('occasion', 'casual'),
            gender=data.get('gender', 'other'),
            favorite_colors=data.get('favorite_colors', 'any'),
            budget=data.get('budget', 'mid'),
            style_type=data.get('style_type', 'casual')
        )
        
        return jsonify({
            'success': True,
            'recommendation': recommendation,
            'occasion': data.get('occasion')
        }), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/image-analysis', methods=['POST'])
def analyze_image():
    """Analyze uploaded image and provide recommendations"""
    try:
        if 'image' not in request.files:
            return jsonify({'error': 'No image provided'}), 400
        
        file = request.files['image']
        
        if file.filename == '':
            return jsonify({'error': 'No file selected'}), 400
        
        if not allowed_file(file.filename):
            return jsonify({'error': 'File type not allowed'}), 400
        
        filename = secure_filename(file.filename)
        user_id = request.form.get('user_id', 'guest')
        
        # Try real Gemini Vision first, then fallback to mock
        if genai is not None:
            try:
                # Read image data
                image_data = file.read()
                base64_image = base64.b64encode(image_data).decode()
                
                # Analyze with Gemini Vision API
                model = genai.GenerativeModel(GEMINI_VISION_MODEL)
                
                prompt = """Analyze this fashion/clothing image and provide:
                1. Color analysis
                2. Style identification
                3. Matching accessories recommendations
                4. Shoe suggestions
                5. Layering ideas
                6. Styling improvements
                7. Occasions this outfit is suitable for
                
                Be specific and actionable in your recommendations."""
                
                response = model.generate_content([
                    {
                        "mime_type": "image/jpeg" if file.filename.endswith('.jpg') or file.filename.endswith('.jpeg') else f"image/{file.filename.split('.')[-1]}",
                        "data": base64_image
                    },
                    prompt
                ])
                
                # Save to database
                analysis = OutfitAnalysis(
                    user_id=user_id,
                    image_name=filename,
                    analysis_result=response.text
                )
                db.session.add(analysis)
                db.session.commit()
                
                return jsonify({
                    'success': True,
                    'analysis': response.text,
                    'image': filename
                }), 200
            except Exception as gemini_error:
                # Fall through to mock if Gemini fails
                print(f"⚠️  Gemini API error: {gemini_error}, using mock AI")
        
        # Use mock AI as fallback (no need to read image for mock)
        analysis_text = get_mock_image_analysis(filename)
        
        # Save mock analysis to database
        analysis = OutfitAnalysis(
            user_id=user_id,
            image_name=filename,
            analysis_result=analysis_text
        )
        db.session.add(analysis)
        db.session.commit()
        
        return jsonify({
            'success': True,
            'analysis': analysis_text,
            'image': filename
        }), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

@app.route('/api/trends', methods=['POST'])
def get_trends():
    """Get current fashion trends"""
    try:
        data = request.json
        region = data.get('region', 'global')
        
        # Try real Gemini first, then fallback to mock
        if genai is not None:
            try:
                prompt = f"""You are a fashion trend expert. Provide current fashion trends for {region} region in 2026.

                Include:
                1. Trending colors and color palettes
                2. Popular outfit styles and silhouettes
                3. Trending accessories
                4. Fabric and material trends
                5. Seasonal recommendations
                6. Celebrity-inspired looks
                7. Budget-friendly trend ideas

                Make it detailed and actionable."""
                
                model = genai.GenerativeModel(GEMINI_MODEL)
                response = model.generate_content(prompt)
                
                return jsonify({
                    'success': True,
                    'trends': response.text,
                    'region': region
                }), 200
            except Exception as gemini_error:
                # Fall through to mock if Gemini fails
                print(f"⚠️  Gemini API error: {gemini_error}, using mock AI")
        
        # Use mock AI as fallback
        trends = get_mock_trends(region)
        return jsonify({
            'success': True,
            'trends': trends,
            'region': region
        }), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/saved-outfits/<user_id>', methods=['GET'])
def get_saved_outfits(user_id):
    """Get user's saved outfits"""
    try:
        outfits = SavedOutfit.query.filter_by(user_id=user_id).order_by(SavedOutfit.created_at.desc()).all()
        
        return jsonify({
            'success': True,
            'outfits': [{
                'id': outfit.id,
                'description': outfit.outfit_description,
                'accessories': outfit.accessories,
                'tips': outfit.styling_tips,
                'occasion': outfit.occasion,
                'rating': outfit.rating,
                'created_at': outfit.created_at.isoformat()
            } for outfit in outfits]
        }), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/saved-outfits', methods=['POST'])
def save_outfit():
    """Save outfit to favorites"""
    try:
        data = request.json
        
        outfit = SavedOutfit(
            user_id=data.get('user_id', 'guest'),
            outfit_description=data.get('outfit_description'),
            accessories=data.get('accessories'),
            styling_tips=data.get('styling_tips'),
            occasion=data.get('occasion')
        )
        
        db.session.add(outfit)
        db.session.commit()
        
        return jsonify({'success': True, 'outfit_id': outfit.id}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

@app.route('/api/saved-outfits/<int:outfit_id>/rate', methods=['POST'])
def rate_outfit(outfit_id):
    """Rate a saved outfit"""
    try:
        data = request.json
        outfit = SavedOutfit.query.get(outfit_id)
        
        if not outfit:
            return jsonify({'error': 'Outfit not found'}), 404
        
        outfit.rating = data.get('rating', 0)
        db.session.commit()
        
        return jsonify({'success': True, 'message': 'Rating saved'}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

@app.route('/api/stylist-chat', methods=['POST'])
def stylist_chat():
    """Chat with AI fashion stylist"""
    try:
        data = request.json
        message = data.get('message')
        
        # Try real Gemini first, then fallback to mock
        if genai is not None:
            try:
                prompt = f"""You are StyleSense, an AI fashion stylist. Respond to the following user message 
                with helpful fashion advice. Keep your response conversational, friendly, and actionable.
                
                User: {message}
                
                Provide fashion-related advice or suggestions."""
                
                model = genai.GenerativeModel(GEMINI_MODEL)
                response = model.generate_content(prompt)
                
                return jsonify({
                    'success': True,
                    'response': response.text
                }), 200
            except Exception as gemini_error:
                # Fall through to mock if Gemini fails
                print(f"⚠️  Gemini API error: {gemini_error}, using mock AI")
        
        # Use mock AI as fallback
        response = get_mock_chat_response(message)
        return jsonify({
            'success': True,
            'response': response
        }), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Utility functions
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# Create database tables
with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
