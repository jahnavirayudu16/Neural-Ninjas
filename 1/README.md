# StyleSense - AI Fashion Recommender 👗✨

A web application that works like a personal AI fashion stylist powered by Python, Flask, and Google Gemini API.

## 🎯 Project Overview

StyleSense is an intelligent fashion recommendation system that:
- Suggests personalized outfits based on user preferences
- Analyzes uploaded clothing images with AI
- Provides current fashion trend insights
- Saves and rates favorite looks
- Offers real-time chat with an AI stylist

## 📋 Features

### Core Features ✅
1. **User Preference Form** - Collect fashion preferences (occasion, colors, budget, style type)
2. **AI Outfit Generator** - Get personalized outfit suggestions powered by Gemini API
3. **Image-Based Recommendations** - Upload images for AI analysis of clothing items
4. **Trend Insights** - Get current fashion trends by region
5. **Personalized Dashboard** - Save and manage favorite outfits
6. **Rating System** - Rate outfits and build your style profile
7. **Chat Stylist** - Real-time conversation with AI fashion advisor

### Extra Features ✨
- 🌙 Dark/Light theme toggle
- ⭐ Outfit rating system (1-5 stars)
- 💾 Save favorite looks to collection
- 💬 AI chat stylist for instant advice
- 📱 Fully responsive design
- 🎨 Modern gradient UI with smooth animations

## 🏗️ Project Structure

```
StyleSense/
├── backend/
│   ├── app.py                 # Flask application & API endpoints
│   ├── requirements.txt       # Python dependencies
│   └── .env.example          # Environment variables template
│
├── frontend/
│   ├── index.html            # Home page
│   ├── recommendations.html  # Outfit recommendations page
│   ├── image-upload.html     # Image upload & analysis
│   ├── trends.html           # Fashion trends page
│   ├── dashboard.html        # My Looks collection
│   ├── chat.html             # Chat with stylist
│   ├── styles.css            # All styling (responsive)
│   ├── script.js             # Shared JavaScript utilities
│   └── assets/
│       ├── images/           # Image assets
│       └── icons/            # Icon files
│
└── README.md                 # This file
```

## 🚀 Getting Started

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)
- Google Generative AI API key (from [Google AI Studio](https://makersuite.google.com/app/apikey))
- A web browser

### Installation

1. **Clone/Navigate to the project:**
   ```bash
   cd StyleSense
   ```

2. **Set up Backend:**
   ```bash
   cd backend
   pip install -r requirements.txt
   ```

3. **Configure Environment Variables:**
   - Copy `.env.example` to `.env`
   - Add your Gemini API key:
     ```
     GEMINI_API_KEY=your_api_key_here
     FLASK_ENV=development
     DATABASE_URL=sqlite:///stylesense.db
     ```

4. **Run Backend Server:**
   ```bash
   python app.py
   ```
   The server will start at `http://localhost:5000`

5. **Start Frontend:**
   - Navigate to `frontend` directory
   - Open `index.html` in your web browser
   - Or use a local server: `python -m http.server 8000` (then visit `http://localhost:8000`)

## 🔌 API Endpoints

### User Preferences
- **POST** `/api/preferences` - Save user fashion preferences
  ```json
  {
    "user_id": "user_123",
    "occasion": "Party",
    "gender": "Female",
    "favorite_colors": "Pink, White",
    "budget": "Medium",
    "style_type": "Western",
    "body_type": "Average"
  }
  ```

### Recommendations
- **POST** `/api/recommendations` - Get outfit recommendations
  ```json
  {
    "occasion": "Party",
    "gender": "Female",
    "favorite_colors": "Pink, White",
    "budget": "Medium",
    "style_type": "Western",
    "body_type": "Average"
  }
  ```

### Image Analysis
- **POST** `/api/image-analysis` - Analyze uploaded outfit image
  - Form data with image file

### Trends
- **POST** `/api/trends` - Get fashion trends
  ```json
  {
    "region": "India"
  }
  ```

### Saved Outfits
- **GET** `/api/saved-outfits/<user_id>` - Get user's saved outfits
- **POST** `/api/saved-outfits` - Save new outfit
- **POST** `/api/saved-outfits/<outfit_id>/rate` - Rate outfit

### Chat
- **POST** `/api/stylist-chat` - Chat with AI stylist
  ```json
  {
    "message": "What should I wear to a casual party?"
  }
  ```

## 🗄️ Database Models

### UserPreference
- user_id, occasion, gender, favorite_colors, budget, style_type, body_type
- Timestamps: created_at, updated_at

### SavedOutfit
- user_id, outfit_description, accessories, styling_tips, occasion, rating
- Timestamp: created_at

### OutfitAnalysis
- user_id, image_name, analysis_result
- Timestamp: created_at

## 🎨 Technology Stack

**Backend:**
- Flask 2.3.3 - Web framework
- Flask-CORS - Cross-origin resource sharing
- Flask-SQLAlchemy - ORM
- Python-dotenv - Environment variables
- Google Generative AI - Gemini API
- Pillow - Image processing

**Frontend:**
- HTML5
- CSS3 (with CSS Variables, Grid, Flexbox)
- Vanilla JavaScript
- Responsive Design

**Database:**
- SQLite (development)

**AI:**
- Google Gemini Pro (text generation)
- Google Gemini Pro Vision (image analysis)

## 💡 How to Use

### Get Outfit Recommendations
1. Go to "Recommendations" page
2. Fill in your preferences (occasion, style, colors, budget)
3. Click "Get Outfit Recommendations"
4. View AI-generated suggestions
5. Save your favorite looks

### Upload and Analyze Images
1. Go to "Upload" page
2. Drag-drop or click to upload an outfit image
3. AI analyzes the clothing and provides:
   - Color analysis
   - Style identification
   - Accessory suggestions
   - Styling improvements

### View Fashion Trends
1. Go to "Trends" page
2. Select a region
3. Get latest fashion trends for that region

### Chat with Stylist
1. Go to "Chat Stylist" page
2. Ask any fashion-related questions
3. Get instant advice from AI

### Manage Saved Looks
1. Go to "My Looks" dashboard
2. View all saved outfits
3. Rate outfits (1-5 stars)
4. Delete outfits

## 🌙 Theme Toggle
- Click the moon/sun button in navigation bar
- Switches between dark and light themes
- Preference is saved in localStorage

## 🔧 Configuration

### Customize Colors
Edit CSS variables in `styles.css`:
```css
:root {
    --primary-color: #667eea;
    --secondary-color: #764ba2;
    --accent-color: #f093fb;
    /* ... more variables */
}
```

### Adjust API Settings
In `backend/app.py`:
- Change `MAX_CONTENT_LENGTH` for file upload size
- Modify `ALLOWED_EXTENSIONS` for supported image formats
- Adjust database URL in `.env`

## 🚨 Error Handling

The application includes comprehensive error handling:
- API validation and error responses
- Image upload validation
- Database error handling
- Network error messages
- User-friendly error notifications

## 📱 Responsive Design

The application is fully responsive and works on:
- Desktop browsers (1200px+)
- Tablets (768px - 1199px)
- Mobile devices (<768px)

Media queries automatically adjust:
- Navigation layout
- Form layouts
- Grid layouts
- Font sizes

## 🔐 Security Considerations

- Store API keys in `.env` (never commit!)
- Validate all user inputs on backend
- Sanitize file uploads
- Use CORS carefully in production
- Implement rate limiting for APIs
- Add user authentication for production

## 🐛 Troubleshooting

### API Connection Error
- Ensure backend is running on port 5000
- Check CORS is properly configured
- Verify .env file has correct settings

### Gemini API Errors
- Verify API key is correct and active
- Check internet connection
- Ensure API account has sufficient quota

### Image Upload Issues
- Check file size doesn't exceed 16MB
- Use supported formats (JPG, PNG, GIF)
- Verify browser permissions

### Database Errors
- Delete `stylesense.db` to reset database
- Check database path in .env
- Ensure write permissions in folder

## 📚 API Documentation

Full API documentation can be viewed when the server is running at:
- `/api/` - All endpoints return JSON responses

## 🎓 Learning Resources

- [Flask Documentation](https://flask.palletsprojects.com/)
- [Google Generative AI API](https://ai.google.dev/)
- [SQLAlchemy ORM](https://www.sqlalchemy.org/)
- [MDN Web Docs](https://developer.mozilla.org/)

## 🤝 Contributing

Feel free to enhance StyleSense:
- Add more features
- Improve UI/UX
- Optimize performance
- Fix bugs
- Add more AI capabilities

## 📄 License

This project is open source and available for educational and commercial use.

## 👨‍💻 Author

Created with ❤️ by AI Fashion Team

---

**Happy Styling! 👗✨**

For questions or support, please refer to the documentation or create an issue.
