# StyleSense Architecture 🏗️

## System Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                      USER BROWSER                            │
│  ┌──────────────────────────────────────────────────────┐   │
│  │  Frontend (HTML/CSS/JavaScript)                      │   │
│  │  ├─ index.html (Home)                                │   │
│  │  ├─ recommendations.html (Outfit Generator)          │   │
│  │  ├─ image-upload.html (Image Analysis)               │   │
│  │  ├─ trends.html (Fashion Trends)                     │   │
│  │  ├─ dashboard.html (My Looks)                        │   │
│  │  ├─ chat.html (Chat Stylist)                         │   │
│  │  ├─ styles.css (Styling)                             │   │
│  │  └─ script.js (Utilities)                            │   │
│  └──────────────────────────────────────────────────────┘   │
│                          ↓ HTTP/REST                        │
│                 (API calls with JSON)                        │
└─────────────────────────────────────────────────────────────┘
                          ↓
┌─────────────────────────────────────────────────────────────┐
│                   BACKEND SERVER                             │
│  ┌──────────────────────────────────────────────────────┐   │
│  │  Flask Application (Python)                          │   │
│  │  ├─ app.py (Main Flask App)                          │   │
│  │  ├─ Routes (API Endpoints)                           │   │
│  │  ├─ Models (SQLAlchemy ORM)                          │   │
│  │  │  ├─ UserPreference                                │   │
│  │  │  ├─ SavedOutfit                                   │   │
│  │  │  └─ OutfitAnalysis                                │   │
│  │  └─ Utilities                                         │   │
│  └──────────────────────────────────────────────────────┘   │
│                          ↓↑                                  │
│  ┌──────────────────────────────────────────────────────┐   │
│  │  Database (SQLAlchemy + SQLite)                      │   │
│  │  ├─ user_preference (user data)                      │   │
│  │  ├─ saved_outfit (collections)                       │   │
│  │  └─ outfit_analysis (image analyses)                 │   │
│  └──────────────────────────────────────────────────────┘   │
│                          ↓↑                                  │
│  ┌──────────────────────────────────────────────────────┐   │
│  │  External API Integration                            │   │
│  │  └─ Google Gemini API                                │   │
│  │     ├─ Gemini Pro (Text Generation)                  │   │
│  │     └─ Gemini Vision (Image Analysis)                │   │
│  └──────────────────────────────────────────────────────┘   │
└─────────────────────────────────────────────────────────────┘
```

---

## Data Flow Diagram

### 1. Getting Outfit Recommendations

```
User Fills Form
    ↓
Frontend Collects Data
    ↓
POST /api/recommendations
    ↓
Flask Receives Request
    ↓
Saves to UserPreference table
    ↓
Builds Gemini Prompt
    ↓
Calls Gemini API
    ↓
Receives AI Recommendation
    ↓
Returns JSON Response
    ↓
Frontend Displays Results
    ↓
User Saves to Collection (Optional)
```

### 2. Image Upload & Analysis

```
User Selects Image
    ↓
Frontend Preview
    ↓
POST /api/image-analysis (FormData)
    ↓
Flask Validates File
    ↓
Encodes Image to Base64
    ↓
Calls Gemini Vision API
    ↓
Receives Analysis
    ↓
Saves to OutfitAnalysis table
    ↓
Returns Analysis JSON
    ↓
Frontend Displays Analysis
```

### 3. Chat Flow

```
User Types Message
    ↓
POST /api/stylist-chat
    ↓
Flask Receives Message
    ↓
Builds Chat Prompt
    ↓
Calls Gemini API
    ↓
Receives Response
    ↓
Returns JSON
    ↓
Frontend Displays in Chat UI
```

---

## API Request/Response Pattern

### Standard Response Format

**Success (200):**
```json
{
  "success": true,
  "data": { ... },
  "message": "Operation successful"
}
```

**Error (400-500):**
```json
{
  "error": "Error description here"
}
```

---

## Database Schema Relationships

```
┌────────────────────────┐
│   UserPreference       │
├────────────────────────┤
│ id (PK)               │
│ user_id               │
│ occasion              │
│ gender                │
│ favorite_colors       │
│ budget                │
│ style_type            │
│ body_type             │
│ created_at            │
│ updated_at            │
└────────────────────────┘

┌────────────────────────┐
│   SavedOutfit          │
├────────────────────────┤
│ id (PK)               │
│ user_id (FK→User)     │
│ outfit_description    │
│ accessories           │
│ styling_tips          │
│ occasion              │
│ rating (0-5)          │
│ created_at            │
└────────────────────────┘

┌────────────────────────┐
│   OutfitAnalysis       │
├────────────────────────┤
│ id (PK)               │
│ user_id (FK→User)     │
│ image_name            │
│ analysis_result       │
│ created_at            │
└────────────────────────┘
```

---

## API Endpoints Structure

### Preference Endpoints
```
POST /api/preferences
├─ Request: User preferences JSON
├─ Response: Success confirmation
└─ Database: Create/Update UserPreference
```

### Recommendation Endpoints
```
POST /api/recommendations
├─ Request: User preferences
├─ Call: Gemini Pro API
├─ Response: Outfit suggestion
└─ Database: (Optional) Save to SavedOutfit
```

### Image Analysis Endpoints
```
POST /api/image-analysis
├─ Request: FormData with image file
├─ Validation: File type & size check
├─ Call: Gemini Vision API
├─ Database: Save to OutfitAnalysis
└─ Response: Analysis results
```

### Trends Endpoints
```
POST /api/trends
├─ Request: Region
├─ Call: Gemini Pro API
└─ Response: Trend data
```

### Outfit Management Endpoints
```
GET /api/saved-outfits/<user_id>
├─ Query: All outfits for user
└─ Response: Array of outfits

POST /api/saved-outfits
├─ Request: Outfit data
├─ Database: Create SavedOutfit
└─ Response: Outfit ID

POST /api/saved-outfits/<outfit_id>/rate
├─ Request: Rating (1-5)
├─ Database: Update SavedOutfit
└─ Response: Confirmation
```

### Chat Endpoints
```
POST /api/stylist-chat
├─ Request: User message
├─ Call: Gemini Pro API (chat context)
└─ Response: AI response
```

---

## Frontend Architecture

### Page Structure

```
frontend/
├── index.html
│   ├── Navigation (shared navbar)
│   ├── Hero section
│   ├── Features grid
│   ├── How it works
│   └── CTA section
│
├── recommendations.html
│   ├── Navigation
│   ├── Preference form
│   ├── Loading state
│   └── Results display
│
├── image-upload.html
│   ├── Navigation
│   ├── Upload area (drag-drop)
│   ├── Preview
│   ├── Analysis button
│   └── Results display
│
├── trends.html
│   ├── Navigation
│   ├── Region selector
│   └── Trends display
│
├── dashboard.html
│   ├── Navigation
│   ├── Outfits grid
│   ├── Modal for details
│   ├── Rating interface
│   └── Delete option
│
├── chat.html
│   ├── Navigation
│   ├── Chat message display
│   └── Chat input form
│
├── styles.css
│   ├── CSS variables (colors)
│   ├── Global styles
│   ├── Component styles
│   ├── Layout (grid/flex)
│   ├── Theme support
│   └── Responsive breakpoints
│
└── script.js
    ├── Theme toggle
    ├── Modal handling
    ├── Utilities
    └── Event listeners
```

### Frontend State Management

```
LocalStorage:
├── theme (light/dark)
└── userId (current user)

SessionStorage:
├── currentRecommendation
└── currentOutfits

In-Memory (JavaScript):
├── window.outfitsData
├── window.currentRecommendation
└── Various form states
```

---

## Backend Code Structure

### Flask App Organization

```
app.py
├── Imports & Configuration
├── Database Configuration
│   ├── SQLAlchemy setup
│   └── Upload folder config
├── Gemini API Configuration
├── Database Models
│   ├── UserPreference class
│   ├── SavedOutfit class
│   └── OutfitAnalysis class
├── API Routes
│   ├── GET / (health check)
│   ├── POST /api/preferences
│   ├── POST /api/recommendations
│   ├── POST /api/image-analysis
│   ├── POST /api/trends
│   ├── GET /api/saved-outfits/<id>
│   ├── POST /api/saved-outfits
│   ├── POST /api/saved-outfits/<id>/rate
│   └── POST /api/stylist-chat
├── Utility Functions
│   ├── allowed_file()
│   └── db initialization
└── Main Execution
```

---

## Authentication & Security

### Current Implementation (Basic)
- User ID based (generated via timestamp)
- No session management
- No authentication required

### For Production, Add:
1. User authentication (JWT tokens)
2. Password hashing (bcrypt)
3. Rate limiting (flask-limiter)
4. HTTPS/SSL
5. API key validation
6. Input sanitization
7. CORS policy refinement
8. Database access control

---

## Error Handling Flow

```
User Action
    ↓
Frontend Validation
    ├─ Empty fields check
    ├─ File type validation
    └─ File size validation
    ↓
API Request
    ↓
Backend Validation
    ├─ Input validation
    ├─ File validation
    └─ Database checks
    ↓
External API Call (Gemini)
    ├─ API key validation
    ├─ Network errors
    └─ API response handling
    ↓
Database Operation
    ├─ Transaction handling
    └─ Rollback on error
    ↓
Response to Frontend
    ├─ Success: JSON data
    └─ Error: Error message
    ↓
Frontend Display
    ├─ Success: Results
    ├─ Error: Error message
    └─ Loading: Spinner
```

---

## Performance Considerations

### Frontend Optimization
- Minimize CSS/JS
- Image compression
- Lazy loading (potential)
- Responsive images
- Caching with localStorage

### Backend Optimization
- Database indexing on user_id
- Connection pooling
- Request validation early
- Error handling efficiency
- API rate limiting

### API Optimization
- Pagination (future)
- Response compression
- Caching headers
- Async processing (future)
- Batch operations (future)

---

## Scalability Path

### Current (Single Server)
```
Frontend → Flask Server → SQLite → Gemini API
```

### Medium Scale
```
Frontend CDN → Load Balancer → Multiple Flask Servers → PostgreSQL → Gemini API
                                     ↓
                              Redis Cache
```

### Large Scale
```
React SPA → CDN → API Gateway → Microservices → Database Cluster → Gemini API
                                    ├─ Recommendations Service
                                    ├─ Image Analysis Service
                                    ├─ Chat Service
                                    └─ Trends Service
```

---

## Technology Justification

| Technology | Why Chosen |
|-----------|-----------|
| Flask | Lightweight, easy to learn, great for APIs |
| SQLite | Simple for development, SQLAlchemy support |
| Vanilla JS | No dependencies, lightweight, learning |
| CSS Grid/Flex | Modern, responsive, no framework needed |
| Gemini API | Affordable, good quality, easy integration |

---

## Testing Approach

### Manual Testing Checklist
- [ ] Form submission
- [ ] API responses
- [ ] Image upload
- [ ] Theme toggle
- [ ] Rating system
- [ ] Save/delete operations
- [ ] Responsive design
- [ ] Error handling

### Automated Testing (Future)
- Unit tests (pytest)
- Integration tests
- E2E tests (Selenium)
- Load testing

---

## Deployment Architecture

### Development
```
localhost:5000 (Backend) + file:/// (Frontend)
```

### Production Options

**Option 1: Heroku**
```
GitHub → Heroku → PostgreSQL → Gemini API
```

**Option 2: AWS**
```
GitHub → EC2 → RDS → Gemini API
         ALB
         S3 (frontend)
```

**Option 3: Docker**
```
Docker Compose → Flask Container → PostgreSQL Container
                Frontend Container (nginx)
```

---

## File Organization Best Practices

### Current Structure
```
✅ Separation of concerns (frontend/backend)
✅ Clear file naming
✅ Organized directory structure
✅ Configuration files separate
✅ Documentation at root
```

### Future Improvements
```
backend/
├── config.py
├── models/
│   └── outfit_models.py
├── routes/
│   ├── preferences.py
│   ├── recommendations.py
│   └── image.py
├── services/
│   ├── gemini_service.py
│   └── outfit_service.py
└── utils/
    └── validators.py
```

---

## Documentation Map

| Document | Purpose |
|----------|---------|
| README.md | Complete project guide |
| QUICKSTART.md | 5-minute setup |
| PROJECT_SUMMARY.md | What was built |
| ARCHITECTURE.md | System design (this file) |
| Code Comments | Implementation details |

---

This architecture supports the current implementation and provides a foundation for future scaling and enhancement!
