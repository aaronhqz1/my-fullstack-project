# 🚀 Fullstack Application

A complete fullstack application built with **FastAPI**, **React (TypeScript)**, and **NestJS**.

## 📋 Table of Contents

- [Tech Stack](#tech-stack)
- [Project Structure](#project-structure)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Running the Application](#running-the-application)
- [API Endpoints](#api-endpoints)
- [Environment Variables](#environment-variables)
- [Development](#development)
- [Troubleshooting](#troubleshooting)

---

## 🛠️ Tech Stack

### Backend
- **FastAPI** - Modern Python web framework for building APIs
- **NestJS** - Progressive Node.js framework for building server-side applications
- **SQLAlchemy** - SQL toolkit and ORM
- **Pydantic** - Data validation using Python type annotations

### Frontend
- **React 18** - JavaScript library for building user interfaces
- **TypeScript** - Typed superset of JavaScript
- **Vite** - Next generation frontend tooling
- **Axios** - Promise-based HTTP client

---

## 📁 Project Structure

```
my-fullstack-project/
├── fastapi-backend/          # FastAPI backend
│   ├── venv/                 # Python virtual environment
│   ├── main.py               # FastAPI application
│   ├── requirements.txt      # Python dependencies
│   └── .env                  # Environment variables
├── react-frontend/           # React frontend
│   ├── src/
│   │   ├── App.tsx           # Main React component
│   │   └── main.tsx          # Entry point
│   ├── package.json          # Node dependencies
│   └── vite.config.ts        # Vite configuration
├── nestjs-backend/           # NestJS backend
│   ├── src/
│   │   ├── main.ts           # NestJS entry point
│   │   ├── app.module.ts     # Root module
│   │   └── app.controller.ts # Main controller
│   ├── package.json          # Node dependencies
│   └── nest-cli.json         # NestJS CLI configuration
├── .gitignore                # Git ignore rules
└── README.md                 # This file
```

---

## ✅ Prerequisites

Make sure you have the following installed:

- **Python 3.8+** - [Download here](https://www.python.org/downloads/)
- **Node.js 18+** - [Download here](https://nodejs.org/)
- **npm** or **yarn** - Comes with Node.js
- **Git** - [Download here](https://git-scm.com/)

### Verify Installation

```bash
python --version
node --version
npm --version
```

---

## 🔧 Installation

### 1. Clone the Repository

```bash
git clone <your-repository-url>
cd my-fullstack-project
```

### 2. Setup FastAPI Backend

```bash
cd fastapi-backend

# Create virtual environment
python -m venv venv

# Activate virtual environment
# Windows CMD:
venv\Scripts\activate.bat
# Windows PowerShell:
venv\Scripts\Activate.ps1
# Mac/Linux:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Return to root
cd ..
```

### 3. Setup React Frontend

```bash
cd react-frontend

# Install dependencies
npm install

# Return to root
cd ..
```

### 4. Setup NestJS Backend

```bash
cd nestjs-backend

# Install dependencies
npm install

# Return to root
cd ..
```

---

## 🚀 Running the Application

You need to run **3 separate terminals** for each service:

### Terminal 1: FastAPI Backend

```bash
cd fastapi-backend
venv\Scripts\activate.bat
uvicorn main:app --reload
```

**Runs on:** http://localhost:8000

### Terminal 2: React Frontend

```bash
cd react-frontend
npm run dev
```

**Runs on:** http://localhost:5173

### Terminal 3: NestJS Backend

```bash
cd nestjs-backend
npm run start:dev
```

**Runs on:** http://localhost:3001

---

## 🌐 API Endpoints

### FastAPI (Port 8000)

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/` | Welcome message |
| GET | `/docs` | Swagger documentation |
| GET | `/api/items` | Get all items |
| POST | `/api/items` | Create new item |
| GET | `/api/health` | Health check |

### NestJS (Port 3001)

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/api` | Welcome message |
| GET | `/api/items` | Get all items |
| POST | `/api/items` | Create new item |
| GET | `/api/health` | Health check |

### React Frontend (Port 5173)

- Main application interface
- Fetches and displays data from both backends

---

## 🔐 Environment Variables

### FastAPI (.env)

Create a `.env` file in `fastapi-backend/`:

```env
DATABASE_URL=sqlite:///./test.db
SECRET_KEY=your-secret-key-change-this
```

### NestJS (.env)

Create a `.env` file in `nestjs-backend/`:

```env
PORT=3001
DATABASE_URL=your-database-url
```

---

## 💻 Development

### FastAPI Development

```bash
# Run with auto-reload
uvicorn main:app --reload

# Run on different port
uvicorn main:app --reload --port 8080

# Run with logging
uvicorn main:app --reload --log-level debug
```

### React Development

```bash
# Start dev server
npm run dev

# Build for production
npm run build

# Preview production build
npm run preview
```

### NestJS Development

```bash
# Start in watch mode
npm run start:dev

# Build for production
npm run build

# Run production build
npm run start:prod

# Generate new resource
nest generate resource users
```

---

## 🐛 Troubleshooting

### Port Already in Use

**Find process using port:**
```bash
# Windows
netstat -ano | findstr :8000

# Kill process
taskkill /PID <PID> /F
```

### Python Virtual Environment Issues

**PowerShell execution policy error:**
```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

### CORS Errors

Make sure CORS is properly configured in both backends:
- FastAPI: Check `app.add_middleware()` in `main.py`
- NestJS: Check `app.enableCors()` in `main.ts`

### Module Not Found Errors

**FastAPI:**
```bash
cd fastapi-backend
venv\Scripts\activate
pip install -r requirements.txt
```

**React/NestJS:**
```bash
rm -rf node_modules
npm install
```

---

## 📦 Building for Production

### FastAPI

```bash
# No build needed, just deploy with:
gunicorn -w 4 -k uvicorn.workers.UvicornWorker main:app
```

### React

```bash
cd react-frontend
npm run build
# Output will be in dist/
```

### NestJS

```bash
cd nestjs-backend
npm run build
npm run start:prod
```

---

## 🧪 Testing

### FastAPI

```bash
cd fastapi-backend
pytest
```

### React

```bash
cd react-frontend
npm test
```

### NestJS

```bash
cd nestjs-backend
npm run test
npm run test:e2e
```

---

## 📝 License

This project is licensed under the MIT License.

---

## 👥 Contributors

- Your Name - Initial work

---

## 🙏 Acknowledgments

- FastAPI Documentation
- React Documentation
- NestJS Documentation

---

## 📧 Contact

For questions or support, please contact: your-email@example.com

---

**Happy Coding! 🎉**