# 🎯 StyleSense Setup Checklist

## Pre-Setup Checklist ✅

- [ ] Python 3.8+ installed on your computer
- [ ] Text editor or IDE (VS Code recommended)
- [ ] Internet connection for API calls
- [ ] Google account (for Gemini API)

---

## Step-by-Step Setup

### 1️⃣ Get Your Gemini API Key (5 minutes)

- [ ] Go to https://makersuite.google.com/app/apikey
- [ ] Sign in with your Google account
- [ ] Click "Create API Key"
- [ ] Copy the key to clipboard
- [ ] Store it safely (you'll need it next)

**⚠️ Important:** Keep your API key secret! Don't share it or commit to GitHub.

---

### 2️⃣ Download/Navigate to Project (2 minutes)

- [ ] Navigate to `c:\AI Fashion Recommender\StyleSense`
- [ ] You should see these folders:
  - ✅ `backend/`
  - ✅ `frontend/`
  - ✅ Documentation files

---

### 3️⃣ Install Python Dependencies (5 minutes)

**For Windows:**
```bash
cd backend
pip install -r requirements.txt
```

**For Mac/Linux:**
```bash
cd backend
pip install -r requirements.txt
```

Wait for all packages to install...

- [ ] Installation complete (should show "Successfully installed...")

---

### 4️⃣ Configure Environment Variables (2 minutes)

1. Navigate to `backend` folder
2. Open `.env.example` file
3. Create a new file named `.env`
4. Copy contents from `.env.example`
5. Replace `your_gemini_api_key_here` with your actual key:

```
GEMINI_API_KEY=YOUR_ACTUAL_KEY_HERE
FLASK_ENV=development
DATABASE_URL=sqlite:///stylesense.db
```

- [ ] `.env` file created
- [ ] API key added
- [ ] File saved

---

### 5️⃣ Start Backend Server (3 minutes)

1. Open terminal/command prompt
2. Navigate to `backend` folder:
```bash
cd backend
```

3. Run Flask app:
```bash
python app.py
```

4. You should see:
```
 * Running on http://127.0.0.1:5000
```

- [ ] Server is running
- [ ] No errors in terminal

**🎯 Keep this terminal open!** The backend needs to stay running.

---

### 6️⃣ Open Frontend (2 minutes)

**Option A: Direct (Easiest)**
1. Navigate to `frontend` folder
2. Double-click `index.html`
3. Opens in your default browser

- [ ] Browser opened with home page

**Option B: Local Server**
1. Open new terminal
2. Navigate to `frontend` folder:
```bash
cd frontend
```

3. Run local server:
```bash
# Windows
py -m http.server 8000

# Mac/Linux
python -m http.server 8000
```

4. Open browser and go to: `http://localhost:8000`

- [ ] Frontend loaded in browser

---

## ✨ First Run Tests

### Test 1: Navigation
- [ ] Click through all navbar links
- [ ] All pages load without errors
- [ ] Theme toggle works (🌙 button)

### Test 2: Get Recommendations
- [ ] Go to "Recommendations" page
- [ ] Fill in all form fields:
  - Select "Casual" occasion
  - Select "Female" gender
  - Enter "Blue, White" for colors
  - Select "Medium" budget
  - Select "Western" style
- [ ] Click "Get Outfit Recommendations"
- [ ] Wait for loading spinner
- [ ] See AI recommendation appear
- [ ] Click "Save This Outfit"
- [ ] See success message

### Test 3: View Saved Looks
- [ ] Go to "My Looks" page
- [ ] See your saved outfit
- [ ] Click outfit card
- [ ] See details modal
- [ ] Rate outfit (click stars)
- [ ] Close modal

### Test 4: Chat Stylist
- [ ] Go to "Chat Stylist"
- [ ] Type: "What should I wear to a casual party?"
- [ ] Press Send
- [ ] See AI response appear

### Test 5: Get Trends
- [ ] Go to "Trends" page
- [ ] Select "India" region
- [ ] Click "Get Trends"
- [ ] See fashion trends

### Test 6: Upload Image (Optional)
- [ ] Go to "Upload" page
- [ ] Find an outfit image on your computer
- [ ] Drag-drop or click to upload
- [ ] Click "Analyze Image"
- [ ] See AI analysis

---

## 🆘 Troubleshooting

### ❌ Backend won't start
```
Error: ModuleNotFoundError
```
**Solution:**
- Run: `pip install -r requirements.txt` again
- Check Python version: `python --version`

### ❌ API Key error
```
Error: GEMINI_API_KEY not found
```
**Solution:**
- Verify `.env` file exists in `backend` folder
- Check API key is correct (copy from Google AI Studio)
- No extra spaces before/after key

### ❌ "Cannot connect to localhost:5000"
```
Error: Connection refused
```
**Solution:**
- Check backend terminal is running `python app.py`
- Check port 5000 is not blocked
- Try port 5001: Edit `app.py` last line to `port=5001`

### ❌ CORS Error
```
Error: Access to XMLHttpRequest blocked by CORS
```
**Solution:**
- Restart Flask backend: Ctrl+C then `python app.py`
- Refresh browser (Ctrl+F5)
- Check API_URL in HTML files matches backend URL

### ❌ Image upload not working
```
Error: File type not allowed
```
**Solution:**
- Use JPG, PNG, or GIF format
- Keep file size under 16MB
- Check browser console for specific error

### ❌ "Database is locked"
```
Error: database is locked
```
**Solution:**
- Delete `backend/stylesense.db` file
- Restart Flask server
- Database will recreate automatically

---

## ✅ Success Indicators

You'll know everything is working when:

1. ✅ Backend runs without errors
2. ✅ Frontend homepage loads
3. ✅ All navbar links work
4. ✅ Theme toggle switches colors
5. ✅ Form submission works
6. ✅ AI recommendations appear
7. ✅ Outfits can be saved
8. ✅ Chat responds with messages
9. ✅ My Looks dashboard shows saved items
10. ✅ No red errors in browser console

---

## 📁 Project Structure Check

Verify you have these files:

```
StyleSense/
├── backend/
│   ├── app.py ✅
│   ├── requirements.txt ✅
│   └── .env.example ✅
├── frontend/
│   ├── index.html ✅
│   ├── recommendations.html ✅
│   ├── image-upload.html ✅
│   ├── trends.html ✅
│   ├── dashboard.html ✅
│   ├── chat.html ✅
│   ├── styles.css ✅
│   └── script.js ✅
├── README.md ✅
├── QUICKSTART.md ✅
├── PROJECT_SUMMARY.md ✅
├── ARCHITECTURE.md ✅
└── manage_db.py ✅
```

---

## 🚀 Ready to Use Commands

### Start Backend
```bash
cd backend
python app.py
```

### Start Frontend (if using server)
```bash
cd frontend
python -m http.server 8000
```

### Reset Database
```bash
python manage_db.py reset
```

### Check Database Stats
```bash
python manage_db.py stats
```

---

## 📚 Documentation to Read

**Quick References:**
1. Start here: `QUICKSTART.md` (5 min read)
2. Full guide: `README.md` (15 min read)
3. Architecture: `ARCHITECTURE.md` (10 min read)
4. Summary: `PROJECT_SUMMARY.md` (5 min read)

---

## 🎯 Common Tasks

### Change Port
Edit `backend/app.py` last line:
```python
# Change 5000 to 8080
app.run(debug=True, port=8080)
```

### Change Theme Colors
Edit `frontend/styles.css`:
```css
:root {
    --primary-color: #667eea;  /* Change this */
    --secondary-color: #764ba2; /* And this */
}
```

### Add New Occasion
Edit `recommendations.html`:
```html
<option value="Your_Occasion">Your Occasion</option>
```

### Change API URL
Search and replace in all HTML files:
```javascript
const API_URL = 'http://localhost:5000/api';
```

---

## 📞 Help Resources

| Issue | Help |
|-------|------|
| Setup Help | See QUICKSTART.md |
| API Help | See README.md #API Endpoints |
| Feature Help | See PROJECT_SUMMARY.md |
| Design Help | See ARCHITECTURE.md |
| Code Help | See code comments |

---

## ✅ Pre-Launch Checklist

Before considering the setup complete:

- [ ] Python installed and working
- [ ] All dependencies installed
- [ ] `.env` file created with API key
- [ ] Backend server running
- [ ] Frontend loads in browser
- [ ] All pages accessible
- [ ] Theme toggle works
- [ ] At least one test successful
- [ ] No errors in browser console
- [ ] No errors in backend terminal

---

## 🎉 You're All Set!

Once all checkboxes are ticked, you're ready to:
- ✨ Get AI fashion recommendations
- 📷 Upload and analyze outfits
- 📊 Check fashion trends
- 💬 Chat with AI stylist
- 💾 Save your favorite looks
- ⭐ Rate your outfits
- 🌙 Switch between themes

---

## 🚀 Next Steps

1. **Explore Features** - Try all pages and features
2. **Customize** - Change colors, add new occasions
3. **Extend** - Add new features you'd like
4. **Deploy** - Put on the web (see README.md)
5. **Share** - Show your friends! 👗✨

---

## 📝 Notes

- Keep API key secure - never commit .env to GitHub
- Backend needs to stay running while using frontend
- Use Chrome/Firefox for best experience
- Check internet connection for AI API calls
- Clear browser cache if you see old versions

---

**Congratulations! You now have a fully functional AI Fashion Recommender! 🎉**

Questions? Check the documentation or review code comments.

**Happy Styling! 👗✨**
