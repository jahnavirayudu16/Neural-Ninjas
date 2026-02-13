# 🚀 StyleSense Quick Start Guide

## ⚡ Get Started in 5 Minutes

### Step 1: Get Your Gemini API Key 🔑
1. Visit [Google AI Studio](https://makersuite.google.com/app/apikey)
2. Click "Create API Key"
3. Copy your API key

### Step 2: Set Up Backend (Python)

**Windows:**
```bash
cd StyleSense\backend
pip install -r requirements.txt
```

**Mac/Linux:**
```bash
cd StyleSense/backend
pip install -r requirements.txt
```

### Step 3: Configure Environment Variables

1. Open `backend/.env` file
2. Replace `your_gemini_api_key_here` with your actual API key:
```
GEMINI_API_KEY=your_actual_key_here
FLASK_ENV=development
DATABASE_URL=sqlite:///stylesense.db
```

### Step 4: Start Backend Server

```bash
cd backend
python app.py
```

**Expected Output:**
```
 * Running on http://127.0.0.1:5000
```

✅ Backend is now running!

### Step 5: Open Frontend

**Option A: Direct (Simple)**
- Navigate to `frontend` folder
- Double-click `index.html`
- Opens in default browser

**Option B: Local Server (Better)**
```bash
cd frontend
# Mac/Linux
python -m http.server 8000

# Windows
py -m http.server 8000
```
Then open: `http://localhost:8000`

---

## 📖 Feature Walkthrough

### 🏠 Home Page
- Overview of StyleSense
- See all features
- "Get Started" button leads to recommendations

### 🎨 Recommendations Page (`recommendations.html`)
1. Fill in your preferences:
   - **Occasion**: Party, Casual, Office, Wedding, etc.
   - **Gender**: Male, Female, Non-binary
   - **Favorite Colors**: Pink, White, Black (comma-separated)
   - **Budget**: Budget, Medium, Premium, Luxury
   - **Style Type**: Traditional, Western, Streetwear, etc.
   - **Body Type**: Optional

2. Click **"Get Outfit Recommendations"**
3. AI generates personalized outfit suggestions
4. Click **"💾 Save This Outfit"** to save to collection

### 📷 Upload Page (`image-upload.html`)
1. Drag-drop or click to upload outfit image
2. Click **"Analyze Image"**
3. AI analyzes and provides:
   - Color analysis
   - Style identification
   - Accessory recommendations
   - Styling tips

### 📊 Trends Page (`trends.html`)
1. Select a region (Global, India, US, Europe, Asia)
2. Click **"Get Trends"**
3. View current fashion trends for that region

### 💾 My Looks Dashboard (`dashboard.html`)
1. View all saved outfits
2. Click outfit card to view details
3. Rate outfits (⭐ 1-5 stars)
4. Delete outfits you no longer want

### 💬 Chat Stylist (`chat.html`)
1. Type your fashion question
2. Send message
3. Get instant AI response
4. Ask anything about styling!

### 🌙 Dark/Light Theme
- Click moon/sun icon in navbar
- Toggles between dark and light themes
- Your preference is saved

---

## 🔌 Testing API Endpoints

### Test with curl or Postman:

**Get Recommendations:**
```bash
curl -X POST http://localhost:5000/api/recommendations \
  -H "Content-Type: application/json" \
  -d '{
    "occasion": "Party",
    "gender": "Female",
    "favorite_colors": "Pink, White",
    "budget": "Medium",
    "style_type": "Western",
    "body_type": "Average"
  }'
```

**Get Trends:**
```bash
curl -X POST http://localhost:5000/api/trends \
  -H "Content-Type: application/json" \
  -d '{"region": "India"}'
```

**Chat with Stylist:**
```bash
curl -X POST http://localhost:5000/api/stylist-chat \
  -H "Content-Type: application/json" \
  -d '{"message": "What should I wear to a beach party?"}'
```

---

## 🎯 API Base URL
```
http://localhost:5000/api
```

### Available Endpoints:
- `POST /preferences` - Save user preferences
- `POST /recommendations` - Get outfit recommendations
- `POST /image-analysis` - Analyze uploaded image
- `POST /trends` - Get fashion trends
- `GET /saved-outfits/<user_id>` - Get saved outfits
- `POST /saved-outfits` - Save new outfit
- `POST /saved-outfits/<outfit_id>/rate` - Rate outfit
- `POST /stylist-chat` - Chat with AI stylist

---

## 🛠️ Troubleshooting

### ❌ "Cannot connect to localhost:5000"
- Make sure backend is running: `python app.py`
- Check Flask is installed: `pip install flask`

### ❌ "API key error"
- Verify .env file has correct key
- Make sure key is pasted correctly (no extra spaces)
- Try generating a new key from Google AI Studio

### ❌ "Image upload not working"
- Check file size < 16MB
- Use JPG, PNG, or GIF format
- Browser may need refresh

### ❌ "Database error"
- Delete `backend/stylesense.db`
- Restart Flask server
- Database will recreate automatically

### ❌ "CORS error"
- Ensure Flask-CORS is installed: `pip install flask-cors`
- Restart Flask server

---

## 📱 Mobile Testing

The application is fully responsive! Test on:
- Desktop (1200px+)
- Tablet (768px - 1199px)
- Mobile (< 768px)

---

## 💾 Data Storage

All data is stored in:
- **Database**: `backend/stylesense.db` (SQLite)
- **Images**: `backend/uploads/` (uploaded images)
- **Browser**: LocalStorage (theme preference, user ID)

---

## 🎨 Customization

### Change Colors
Edit `frontend/styles.css`:
```css
:root {
    --primary-color: #667eea;      /* Change this */
    --secondary-color: #764ba2;    /* And this */
    --accent-color: #f093fb;       /* And this */
}
```

### Change Port
Edit `backend/app.py` last line:
```python
app.run(debug=True, port=5000)  # Change 5000 to any port
```

### Update API URL
If using different backend URL, edit frontend pages:
```javascript
const API_URL = 'http://localhost:5000/api';  // Change this
```

---

## 🚀 Deployment Tips

### For Production:
1. Set `FLASK_ENV=production` in .env
2. Use a production database (PostgreSQL, MySQL)
3. Deploy to Heroku, AWS, or similar
4. Add user authentication
5. Implement rate limiting
6. Use HTTPS
7. Add API key validation

### Deploy Backend to Heroku:
```bash
heroku login
heroku create your-app-name
git push heroku main
```

---

## 📚 Example Prompts

Try these with the Chat Stylist:

- "What should I wear to a job interview?"
- "How to style a black dress?"
- "Best colors for Indian skin tones?"
- "Outfit ideas for a casual beach day?"
- "How to accessorize minimalist outfits?"

---

## ✨ Pro Tips

1. **Save Favorites**: Always save outfits you like to compare later
2. **Rate Outfits**: Rating helps personalize future suggestions
3. **Upload References**: Upload images of styles you like
4. **Check Trends**: Stay updated with fashion trends
5. **Use Chat**: Ask specific styling questions for tips

---

## 🆘 Need Help?

1. Check README.md for detailed documentation
2. Review API documentation in code comments
3. Check browser console (F12) for errors
4. Verify .env configuration
5. Ensure internet connection is working

---

## 📞 Support

For issues:
1. Check terminal for error messages
2. Review .env configuration
3. Verify API key is valid
4. Check internet connection
5. Restart both backend and frontend

---

**Happy Styling! 👗✨**

Enjoy your personal AI fashion stylist!
