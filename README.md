# Movie Recommendation System - Comprehensive Project Documentation

## Table of Contents
1. [Executive Summary](#executive-summary)
2. [Project Overview](#project-overview)
3. [Technical Architecture](#technical-architecture)
4. [System Components](#system-components)
5. [Recommendation Algorithms](#recommendation-algorithms)
6. [Database Schema](#database-schema)
7. [API Endpoints](#api-endpoints)
8. [Data Pipeline](#data-pipeline)
9. [Frontend Features](#frontend-features)
10. [Authentication & Security](#authentication--security)
11. [Development Status](#development-status)

---

## Executive Summary

The **Movie Recommendation System** is a full-stack web application designed to provide personalized and algorithmic movie recommendations to users. Built with modern web technologies, this platform leverages multiple recommendation algorithms to help users discover movies based on content similarity, popularity trends, and genre preferences. The system integrates a robust backend API with a responsive frontend interface, powered by a MySQL database containing MovieLens dataset information.

**Status**: Under active development

---

## Project Overview

### Purpose
The Movie Recommendation System serves as a comprehensive platform for movie discovery, combining user authentication, watchlist management, and intelligent recommendation algorithms. Users can browse movies, manage personal collections, receive tailored recommendations, and explore trending content across different genres.

### Key Objectives
- Provide multiple recommendation strategies to cater to different user preferences
- Enable seamless user authentication and account management
- Maintain personalized watchlists and viewing histories
- Deliver pre-computed similarity metrics for fast recommendation retrieval
- Create an intuitive user interface for movie discovery

### Target Users
- Movie enthusiasts seeking personalized recommendations
- General users looking to discover new films
- Users interested in trending and popular movies
- Genre-specific content consumers

---

## Technical Architecture

### Architecture Overview
The application follows a **three-tier architecture** pattern:
- **Frontend Tier**: React-based SPA with TypeScript
- **API Tier**: FastAPI-based REST backend
- **Data Tier**: MySQL relational database

### Technology Stack

#### Backend
| Component | Technology | Version/Notes |
|-----------|-----------|--------------|
| Framework | FastAPI | Python web framework for API |
| Language | Python | 3.8+ |
| Database | MySQL | InnoDB storage engine |
| Authentication | JWT | Custom JWT handler utility |
| Password Security | bcrypt-based | Custom pass_handler utility |
| Data Processing | Pandas, NumPy, scikit-learn, SciPy | For ML/data operations |

#### Frontend
| Component | Technology | Version |
|-----------|-----------|---------|
| Framework | React | v19.2.0 |
| Language | TypeScript | Type-safe development |
| Build Tool | Vite | Fast module bundling |
| Styling | Tailwind CSS | v4.2.1 + Tailwind Merge |
| UI Components | Radix UI + shadcn | Component library |
| Routing | React Router | v7.13.1 |
| Theme Management | next-themes | Dark/light mode support |
| Icons | Lucide React | v0.577.0 |
| Dev Server | Vite Dev Server | Port 5173/5174 |

#### Data Processing
| Component | Purpose |
|-----------|---------|
| Jupyter Notebooks | EDA, data cleaning, analysis |
| Pandas/NumPy | Data transformation and manipulation |
| scikit-learn | Machine learning utilities |
| SciPy | Scientific computing for similarity |

### CORS Configuration
The backend is configured to accept requests from:
- `http://localhost:5173`
- `http://127.0.0.1:5173`
- `http://localhost:5174`
- `http://127.0.0.1:5174`

---

## System Components

### Backend Structure

#### Directory Organization
```
backend/
├── __init__.py
├── app.py                          # FastAPI application entry point
├── controllers/                     # Business logic layer
│   ├── account/
│   │   └── account_management_controller.py
│   ├── auth/
│   │   └── users_controller.py
│   ├── movies/
│   │   ├── movie_details_controller.py
│   │   └── movies_controller.py
│   └── recommendation/
│       ├── get_top_genre_movies_controller.py
│       ├── mlt_controller.py           # More Like This
│       ├── mpgl_controller.py           # Most Popular Genre List
│       └── mpoat_controller.py          # Most Popular of All Time
├── database/
│   ├── __init__.py
│   └── database.py                 # Database connection management
├── models/                          # Data models and algorithms
│   ├── account/
│   │   └── account_management_model.py
│   ├── movies/
│   │   ├── movie_details_model.py
│   │   ├── movies_model.py
│   │   ├── ratings_model.py
│   │   └── tags_model.py
│   ├── recommendation/
│   │   ├── get_top_genre_movies.py
│   │   ├── mlt_model.py                # MLT algorithm implementation
│   │   ├── mpgl_model.py               # MPGL algorithm implementation
│   │   └── mpoat_model.py              # MPOAT algorithm implementation
│   └── users/
│       └── users_model.py
├── routers/                         # API route definitions
│   ├── __init__.py
│   ├── auth_route.py               # Authentication endpoints
│   ├── movies_route.py             # Movie management endpoints
│   └── recommendation_route.py     # Recommendation endpoints
├── schemas/                         # Pydantic data validation schemas
│   ├── account_schema.py
│   ├── auth_schema.py
│   ├── movie_schema.py
│   └── user/
│       └── user_schema.py
└── utils/                           # Utility functions
    ├── jwt_handler.py              # JWT token management
    ├── pass_handler.py             # Password hashing/verification
    └── user_authorization.py       # Authorization checks
```

#### Key Components

**app.py**: FastAPI application initialization with CORS middleware configuration

**Controllers**: Implement business logic, bridging routers and models
- Account controllers handle user profile operations
- Auth controllers manage authentication flows
- Movie controllers handle movie operations
- Recommendation controllers execute recommendation algorithms

**Models**: Contain data access logic and algorithm implementations
- Database queries
- Recommendation algorithm computations
- Data transformations

**Routers**: Define API endpoints and request routing
- `/auth/*` - Authentication endpoints
- `/movies/*` - Movie management
- `/recommendations/*` - Recommendation endpoints

**Schemas**: Pydantic models for request/response validation
- Type checking and data validation
- API documentation generation

**Utils**: Cross-cutting concerns
- JWT token generation and verification
- Password hashing and validation
- User authorization middleware

### Frontend Structure

#### Main Components
```
frontend/src/
├── App.jsx                          # Main application component
├── Layout.tsx                       # Main layout wrapper
├── Auth/                            # Authentication pages
│   ├── Login.tsx
│   ├── Signup.tsx
│   ├── ResetPassword.tsx
│   ├── Layout.tsx
│   └── Header&Footer/
├── components/                      # Reusable UI components
│   ├── Loading.tsx
│   ├── mode-toggle.tsx             # Dark/light mode toggle
│   └── ...
├── context/                         # React context for state management
├── Header&Footer/                  # Layout components
├── pages/                           # Page components
├── Route/                           # Routing configuration
├── lib/                             # Utility libraries
├── assets/                          # Static assets
├── App.css                          # Global styles
├── index.css                        # Base styles
├── Tailwind.css                     # Tailwind directives
├── main.tsx                         # Entry point
├── home.tsx                         # Home page
└── vite-env.d.ts                   # Vite environment types
```

#### Frontend Features
- **Authentication Flow**: Login/Signup pages with form validation
- **Movie Discovery**: Browse and search movies
- **Watchlist Management**: Add/remove movies, track viewing status
- **Recommendations Display**: View algorithmic recommendations
- **Dark Mode**: Theme toggle with next-themes
- **Responsive Design**: Mobile-friendly interface with Tailwind CSS

---

## Recommendation Algorithms

### 1. More Like This (MLT)
**Type**: Content-Based Similarity  
**Purpose**: Finds movies similar to a given movie

**Algorithm**:
1. Constructs user-movie rating matrix from ratings data
2. Converts matrix to sparse format for efficiency
3. Computes cosine similarity between all movie pairs
4. Pre-computes and stores top 20 similar movies per movie
5. Returns cached similarity data on request

**Implementation**: `models/recommendation/mlt_model.py`  
**Endpoint**: `GET /recommendations/moreLikeThis/{movie_id}`  
**Output**: Top 20 most similar movies with similarity scores

**Use Case**: "If I liked this movie, what else would I enjoy?"

---

### 2. Most Popular of All Time (MPOAT)
**Type**: Popularity-Based  
**Purpose**: Recommends the most highly-rated movies across entire catalog

**Algorithm**:
1. Aggregates ratings for each movie
2. Calculates weighted rating (considers rating value and frequency)
3. Ranks movies by weighted rating in descending order
4. Returns top 50 movies

**Implementation**: `models/recommendation/mpoat_model.py`  
**Endpoint**: `GET /recommendations/popularMovies`  
**Output**: Top 50 most popular movies of all time

**Use Case**: "Show me the best movies overall"

---

### 3. Most Popular Genre List (MPGL)
**Type**: Genre-Based Popularity  
**Purpose**: Identifies trending and popular genres

**Algorithm**:
1. Groups movies by genre
2. Calculates average rating per genre
3. Counts movies in each genre
4. Ranks genres by combined popularity metrics
5. Returns genre statistics and rankings

**Implementation**: `models/recommendation/mpgl_model.py`  
**Endpoint**: `GET /recommendations/popularGenres`  
**Output**: Ranked list of genres with popularity metrics

**Use Case**: "What are the most popular genres right now?"

---

### 4. Top Genre Movies (TGM)
**Type**: Genre-Specific Popularity  
**Purpose**: Returns top-rated movies within a specific genre

**Algorithm**:
1. Filters movies by specified genre
2. Sorts by weighted rating
3. Returns top 50 movies in that genre
4. Pre-sorted for fast retrieval

**Implementation**: `models/recommendation/get_top_genre_movies.py`  
**Endpoint**: `GET /recommendations/topGenreMovies/{genre_id}`  
**Output**: Top 50 movies in specified genre

**Use Case**: "Show me the best Action movies" or "Top Comedy films"

---

## Database Schema

### Core Tables

#### Users Table
- User identification and credentials
- Account creation timestamp
- Password hash storage (bcrypt)

#### Movies Table
- Movie metadata (title, release year)
- IMDB/TMDB IDs for external linking
- Pre-computed weighted rating
- Overview/description

#### Genres Table
- Genre definitions and categorization

#### Movie-Genre Junction Table
- Many-to-many relationship mapping
- Allows movies to belong to multiple genres

#### Ratings Table
- User-movie rating pairs
- Rating values (typically 0.5 - 5.0 scale)
- Timestamp of rating

#### Tags Table
- User-generated movie tags/keywords
- Tag text and associated movie-user pairs

#### Links Table
- External identifiers (IMDB ID, TMDB ID)
- Movie cross-reference information

#### Movie Similarity Table
- Pre-computed cosine similarity values
- Top 20 similar movies per movie (indexed by movie_id)
- Similarity scores for quick retrieval

### Key Design Decisions
- **InnoDB Storage Engine**: ACID compliance for data integrity
- **Pre-computed Similarities**: Trade storage for query speed
- **Normalization**: Prevent data redundancy, maintain referential integrity
- **Indexing Strategy**: Optimize common query patterns (user ratings, genre lookups)

---

## API Endpoints

### Authentication Endpoints

#### POST `/auth/signup`
Register a new user account
- **Request**: Email, password, user details
- **Response**: User ID, authentication token
- **Status**: 201 Created

#### POST `/auth/login`
Authenticate user and obtain JWT token
- **Request**: Email, password
- **Response**: JWT token, user profile
- **Status**: 200 OK

---

### Movie Endpoints

#### GET `/movies/detail/{movie_id}`
Retrieve comprehensive movie information
- **Response**: Title, plot, genres, ratings, year, external links
- **Status**: 200 OK

#### POST `/movies/addWatchlist`
Add movie to user's watchlist
- **Request**: Movie ID
- **Response**: Updated watchlist
- **Status**: 200 OK

#### POST `/movies/removeWatchList`
Remove movie from user's watchlist
- **Request**: Movie ID
- **Response**: Updated watchlist
- **Status**: 200 OK

#### POST `/movies/markWatched`
Mark a movie as watched in user's history
- **Request**: Movie ID
- **Response**: Updated viewing status
- **Status**: 200 OK

#### GET `/movies/displayWatchlist`
Retrieve user's current watchlist
- **Response**: List of watchlisted movies with metadata
- **Authentication**: Required (JWT)
- **Status**: 200 OK

---

### Recommendation Endpoints

#### GET `/recommendations/popularMovies`
Get the most popular movies of all time
- **Response**: Top 50 movies sorted by weighted rating
- **Query Parameters**: Optional limit/offset
- **Status**: 200 OK

#### GET `/recommendations/popularGenres`
Identify trending genres
- **Response**: Genre rankings with popularity metrics
- **Status**: 200 OK

#### GET `/recommendations/topGenreMovies/{genre_id}`
Get top movies within a specific genre
- **Path Parameter**: genre_id
- **Response**: Top 50 movies in genre by rating
- **Status**: 200 OK

#### GET `/recommendations/moreLikeThis/{movie_id}`
Find similar movies using content-based filtering
- **Path Parameter**: movie_id
- **Response**: Top 20 similar movies with similarity scores
- **Status**: 200 OK

---

### Error Handling
All endpoints include standard HTTP status codes:
- `400 Bad Request`: Invalid parameters
- `401 Unauthorized`: Missing/invalid authentication
- `404 Not Found`: Resource not found
- `500 Internal Server Error`: Server error

---

## Data Pipeline

### Data Sources
**MovieLens Dataset**:
- `movies.csv`: Movie metadata
- `ratings.csv`: User ratings (200k+ ratings from 600+ users)
- `tags.csv`: User-generated tags
- `links.csv`: External identifiers (IMDB, TMDB)

### Data Processing Workflow

```
Raw CSV Files
    ↓
[data_cleaning.ipynb]
    ├─ Data type validation
    ├─ Handle missing values
    ├─ Remove duplicates
    └─ Outlier detection
    ↓
[eda.ipynb]
    ├─ Distribution analysis
    ├─ Correlation studies
    ├─ Genre popularity analysis
    └─ Rating patterns
    ↓
Cleaned Datasets
    (cleaned_datasets/ folder)
    ↓
[db_builder_facade.py]
    ├─ Connection pooling
    ├─ Batch data loading
    └─ Transaction management
    ↓
Data Loading Modules
    ├─ data_loading_users.py → Users table
    ├─ data_loading_movies.py → Movies table
    ├─ data_loading_genres.py → Genres table
    ├─ data_loading_moviegenre.py → Junction table
    ├─ data_loading_rating.py → Ratings table
    ├─ data_loading_tags.py → Tags table
    ├─ data_loading_links.py → Links table
    └─ data_movie_sim_load.py → Movie Similarity table
    ↓
[user_gen.py]
    └─ Synthetic user generation (optional)
    ↓
MySQL Database
    └─ Full normalized dataset ready for queries
```

### Key Processing Steps

1. **Data Cleaning**
   - Handle missing/null values
   - Validate data types
   - Remove corrupted records
   - Standardize formats

2. **Exploratory Data Analysis**
   - Statistical summaries
   - Distribution visualization
   - Correlation analysis
   - Genre and rating patterns

3. **Data Loading**
   - Transactional batch inserts
   - Referential integrity checks
   - Index creation
   - Query optimization

4. **Feature Computation**
   - Weighted rating calculation
   - Cosine similarity matrix
   - Pre-computed recommendations

### Database Builder Facade
**File**: `db_data_loading/db_builder_facade.py`

Orchestrates entire data loading process:
- Connection pool management
- Transaction handling
- Error recovery
- Progress tracking
- Data consistency validation

---

## Frontend Features

### User Interface Components

#### Authentication Pages
- **Login Page**: Email/password credentials with validation
- **Signup Page**: Registration form with password confirmation
- **Reset Password**: Password recovery flow
- **Header & Footer**: Navigation and branding

#### Movie Discovery
- **Movie Browse**: Grid/list view of movies
- **Movie Details**: Full movie information card
  - Title, plot summary, genres
  - Rating and review count
  - External links (IMDB)
  - Similar movies recommendations

#### Watchlist Management
- **Watchlist View**: Display saved movies
- **Add to Watchlist**: Quick-add buttons
- **Remove from Watchlist**: Manage collection
- **Mark as Watched**: Track viewing history

#### Recommendations Display
- **Popular Movies**: Top-rated films carousel
- **Genre Recommendations**: Browse by genre
- **Similar Movies**: Content-based suggestions
- **Personalized Recommendations**: Genre-based suggestions

#### UI/UX Features
- **Dark Mode Toggle**: Light/dark theme switching via next-themes
- **Loading States**: Spinner component for async operations
- **Responsive Design**: Mobile-first approach with Tailwind
- **Icon System**: Lucide React icons for intuitive navigation
- **Component Library**: shadcn/Radix UI for consistent styling

### Styling Approach
- **Tailwind CSS v4.2.1**: Utility-first CSS framework
- **Tailwind Merge**: Smart class merging for component composition
- **tw-animate-css**: Animation utilities
- **Custom CSS**: App-level overrides and theme customization

---

## Authentication & Security

### JWT-Based Authentication

#### Token Structure
- **Header**: Algorithm type (HS256)
- **Payload**: User ID, email, issued timestamp
- **Signature**: Server secret key

#### Implementation
**File**: `backend/utils/jwt_handler.py`

Provides:
- Token generation on login
- Token validation on requests
- Token expiration handling
- Refresh token logic (if implemented)

#### Authorization Middleware
**File**: `backend/utils/user_authorization.py`

Enforces:
- Token presence in request
- Token validity and expiration
- User identity verification
- Protected endpoint access

### Password Security

#### Password Hashing
**File**: `backend/utils/pass_handler.py`

Uses industry-standard bcrypt:
- One-way hashing function
- Salt generation per password
- Configurable work factor
- Resistant to brute-force attacks

#### Password Verification
- Secure comparison functions
- Timing attack resistance
- Salted hash validation

### Protected Endpoints
Endpoints requiring authentication:
- `GET /movies/displayWatchlist`
- `POST /movies/addWatchlist`
- `POST /movies/removeWatchList`
- `POST /movies/markWatched`
- Any personalized recommendation endpoints

### Security Best Practices
- CORS configuration limiting accepted origins
- Pydantic schema validation
- SQL injection prevention (parameterized queries)
- XSS protection (response encoding)
- HTTPS ready (production deployment requirement)

---

## Development Status

### Current Phase
**Alpha Development** - Core features implemented, under active testing

### Completed Features
✅ User authentication system (login/signup)  
✅ Movie database integration (100,000+ movies)  
✅ Four recommendation algorithms  
✅ Watchlist management  
✅ Movie detail views  
✅ Frontend UI components  
✅ API endpoint implementation  
✅ Database schema and data loading pipeline  

### In Development / Planned Features
🔄 Advanced search and filtering  
🔄 User ratings and reviews  
🔄 Personalized recommendations (collaborative filtering)  
🔄 Social features (following, sharing)  
🔄 Performance optimization  
🔄 Comprehensive testing suite  
🔄 Deployment pipeline  
🔄 Analytics and monitoring  

### Known Limitations
- Single-machine deployment
- Pre-computed recommendations (not real-time)
- Limited to MovieLens dataset
- Basic error handling in some modules

### Deployment Considerations
- Backend: FastAPI with Uvicorn/Gunicorn server
- Frontend: Static build output via Vite
- Database: MySQL 8.0+ with InnoDB
- Environment: Python 3.8+, Node.js 18+
- Containerization: Docker configuration recommended

---

## Project Statistics

| Metric | Value |
|--------|-------|
| Movies in Database | 100,000+ |
| Users (Initial) | 610+ |
| Ratings | 200,000+ |
| Genres | 20+ |
| API Endpoints | 10+ |
| Frontend Pages | 6+ |
| Backend Controllers | 10+ |
| Recommendation Algorithms | 4 |
| Lines of Code (Estimated) | 5,000+ |

---

## Getting Started

### Prerequisites
- Python 3.8 or higher
- Node.js 18 or higher
- MySQL 8.0 or higher
- pip and npm package managers

### Backend Setup
```bash
# Navigate to project root
cd movie_rec

# Create Python virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install fastapi uvicorn mysql-connector-python pydantic

# Run database setup
cd data_processing/db_data_loading
python db_builder_facade.py

# Start backend server
uvicorn backend.app:app --reload
```

### Frontend Setup
```bash
# Navigate to frontend directory
cd frontend

# Install dependencies
npm install

# Start development server
npm run dev
```

### Database Setup
1. Create MySQL database
2. Run schema initialization: `schema_initial_create.sql`
3. Load data using db_builder_facade.py
4. Verify data with sample queries

---

## Architecture Diagram

```
┌─────────────────────────────────────────────────────────────┐
│                      USER BROWSER                            │
│              (React 19 + TypeScript + Vite)                  │
├─────────────────────────────────────────────────────────────┤
│                     FRONTEND (Port 5173)                     │
│  ┌──────────────────────────────────────────────────────┐  │
│  │ Routes: Auth, Movies, Recommendations, Watchlist     │  │
│  │ Components: Pages, UI Elements, Navigation           │  │
│  │ State: Context API, React Hooks                      │  │
│  │ Styling: Tailwind CSS, Radix UI, shadcn            │  │
│  └──────────────────────────────────────────────────────┘  │
└────────────┬───────────────────────────────────────────────┘
             │ HTTP/CORS
             ↓
┌─────────────────────────────────────────────────────────────┐
│                    BACKEND API (Port 8000)                   │
│                   (FastAPI + Python)                         │
│  ┌──────────────────────────────────────────────────────┐  │
│  │ Routers: /auth, /movies, /recommendations           │  │
│  │ Controllers: Business logic layer                    │  │
│  │ Models: Data access & algorithms                     │  │
│  │ Utils: JWT, Password, Authorization                 │  │
│  │ Schemas: Pydantic validation                        │  │
│  └──────────────────────────────────────────────────────┘  │
└────────────┬───────────────────────────────────────────────┘
             │ MySQL Protocol
             ↓
┌─────────────────────────────────────────────────────────────┐
│                    MYSQL DATABASE                            │
│  ┌──────────────────────────────────────────────────────┐  │
│  │ Users | Movies | Genres | Movie-Genre               │  │
│  │ Ratings | Tags | Links | Movie Similarity           │  │
│  │ InnoDB Engine, Indexed, Normalized Schema            │  │
│  └──────────────────────────────────────────────────────┘  │
└─────────────────────────────────────────────────────────────┘
                         ↑
                         │
           ┌─────────────┴──────────────┐
           │                             │
   ┌───────────────────┐       ┌───────────────────┐
   │  DATA PIPELINE    │       │   JUPYTER EDA     │
   │ (db_builder_      │       │  & CLEANING       │
   │  facade.py)       │       │  (Notebooks)      │
   │                   │       │                   │
   │ • Connection mgmt │       │ • data_cleaning   │
   │ • Batch loading   │       │ • eda              │
   │ • Transactions    │       │ • report           │
   │ • Data modules    │       │                   │
   └───────────────────┘       └───────────────────┘
           ↑                             ↑
           │                             │
    ┌──────────────────────────────────────────┐
    │   RAW CSV DATA (MovieLens Dataset)        │
    │  • movies.csv                             │
    │  • ratings.csv                            │
    │  • tags.csv                               │
    │  • links.csv                              │
    └──────────────────────────────────────────┘
```

---

## Conclusion

The Movie Recommendation System is a comprehensive, well-architected full-stack application that demonstrates modern web development practices. With multiple recommendation algorithms, secure authentication, and a responsive user interface, it provides a solid foundation for a production-ready movie discovery platform.

The modular design allows for easy feature additions and maintenance, while the pre-computed recommendation data ensures fast query performance even with large datasets. As development continues, this system can be extended with collaborative filtering, advanced search capabilities, and social features to create an even more engaging user experience.

---

**Document Version**: 1.0  
**Last Updated**: 2026-01-01  
**Project Status**: Active Development  
**Maintainer**: Development Team
