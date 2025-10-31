# Global Horizon University Alumni Network

A full-stack web application for university alumni networking, built with FastAPI, React, and MongoDB.

## 🚀 Features

- **User Authentication**: Secure registration and login system
- **Dashboard**: Alumni statistics and photo carousel


## 📋 Prerequisites

- Python 3.11+
- Node.js 18+ and Yarn
- MongoDB

## 🛠️ Installation & Setup

### Method 1: Local Development

1. **Clone the repository**
   ```bash
   git clone <your-repo-url>
   cd global_horizon_alumni
   ```

2. **Backend Setup**
   ```bash
   cd backend
   pip install -r requirements.txt
   ```

3. **Frontend Setup**
   ```bash
   cd frontend
   yarn install
   ```

4. **Environment Variables**
   
   Backend `.env` (in `/backend/.env`):
   ```
   MONGO_URL=mongodb://localhost:27017
   DB_NAME=global_horizon_alumni
   CORS_ORIGINS=*
   JWT_SECRET=your-secret-key-change-in-production
   ```
   
   Frontend `.env` (in `/frontend/.env`):
   ```
   REACT_APP_BACKEND_URL=http://localhost:8001
   WDS_SOCKET_PORT=3000
   ```

5. **Start MongoDB**
   ```bash
   mongod
   ```

6. **Run the Application**
   
   Terminal 1 - Backend:
   ```bash
   cd backend
   uvicorn server:app --host 0.0.0.0 --port 8001 --reload
   ```
   
   Terminal 2 - Frontend:
   ```bash
   cd frontend
   yarn start
   ```

7. **Access the Application**
   - Frontend: http://localhost:3000
   - Backend API: http://localhost:8001
   - API Docs: http://localhost:8001/docs

### Method 2: GitHub Codespaces ⭐

1. **Push to GitHub**
   ```bash
   git init
   git add .
   git commit -m "Initial commit: Global Horizon Alumni Network"
   git branch -M main
   git remote add origin <your-github-repo-url>
   git push -u origin main
   ```

2. **Open in Codespaces**
   - Go to your GitHub repository
   - Click the green "Code" button
   - Select "Codespaces" tab
   - Click "Create codespace on main"

3. **Setup in Codespaces**
   
   Once Codespaces opens, run in the terminal:
   
   ```bash
   # Install backend dependencies
   cd backend
   pip install -r requirements.txt
   cd ..
   
   # Install frontend dependencies
   cd frontend
   yarn install
   cd ..
   ```

4. **Start MongoDB in Codespaces**
   ```bash
   # Install MongoDB (if not already installed)
   wget -qO - https://www.mongodb.org/static/pgp/server-6.0.asc | sudo apt-key add -
   echo "deb [ arch=amd64,arm64 ] https://repo.mongodb.org/apt/ubuntu focal/mongodb-org/6.0 multiverse" | sudo tee /etc/apt/sources.list.d/mongodb-org-6.0.list
   sudo apt-get update
   sudo apt-get install -y mongodb-org
   
   # Start MongoDB
   sudo systemctl start mongod
   ```

5. **Update Environment Variables for Codespaces**
   
   The frontend `.env` needs to point to the Codespaces backend URL.
   Codespaces will automatically forward ports.
   
   **Important**: Find your Codespace URL from the browser address bar.
   It looks like: `https://<your-codespace-name>.github.dev`
   
   Update `/frontend/.env`:
   ```
   REACT_APP_BACKEND_URL=https://<your-codespace-name>-8001.app.github.dev
   ```
   Replace `<your-codespace-name>` with your actual Codespace name

6. **Run the Application in Codespaces**
   
   Open 2 terminals in Codespaces (Terminal → Split Terminal):
   
   **Terminal 1 - Backend:**
   ```bash
   cd backend
   uvicorn server:app --host 0.0.0.0 --port 8001 --reload
   ```
   
   **Terminal 2 - Frontend:**
   ```bash
   cd frontend
   yarn start
   ```

7. **Access in Browser** 🌐
   - Codespaces will show a popup: "Your application running on port 3000 is available"
   - Click "Open in Browser" or
   - Go to the "PORTS" tab (bottom panel in VS Code)
   - Find port 3000, right-click and select "Open in Browser"
   - Or manually visit: `https://<your-codespace-name>-3000.app.github.dev`

## 🎯 Usage Guide

### First Time Setup

1. **Register a New Account**
   - Navigate to the homepage
   - Click "Register Now"
   - Fill in all required fields (Note: Phone must be in US format: (XXX) XXX-XXXX)
   - Submit to auto-login

2. **Explore Features**
   - **Dashboard**: View alumni statistics and photos
   - **Events**: Browse events and register (4 events allow registration)
   - **Connect**: Search for alumni by name/company and start chatting
   - **Donate**: Support university causes ($10-$10,000)
   - **About**: Learn about the university
   - **Contact**: Submit feedback (max 200 words)
   - **Profile**: View and edit your information

### Testing Chat Feature

1. Open the app in 2 different browsers or incognito windows
2. Register 2 different users
3. In one window, go to Connect and search for the other user
4. Start chatting - messages appear in real-time!

## 📁 Project Structure

```
global_horizon_alumni/
├── backend/
│   ├── server.py          # FastAPI application
│   ├── requirements.txt   # Python dependencies
│   └── .env              # Backend environment variables
├── frontend/
│   ├── public/           # Static files
│   ├── src/
│   │   ├── components/   # Reusable components
│   │   │   ├── ui/       # Shadcn UI components
│   │   │   └── Layout.jsx
│   │   ├── pages/        # Page components
│   │   │   ├── Homepage.jsx
│   │   │   ├── Register.jsx
│   │   │   ├── Login.jsx
│   │   │   ├── Dashboard.jsx
│   │   │   ├── Events.jsx
│   │   │   ├── Connect.jsx
│   │   │   ├── Donate.jsx
│   │   │   ├── About.jsx
│   │   │   ├── Contact.jsx
│   │   │   └── Profile.jsx
│   │   ├── App.js        # Main app component
│   │   ├── App.css       # Global styles
│   │   └── index.js      # Entry point
│   ├── package.json      # Node dependencies
│   └── .env             # Frontend environment variables
└── README.md            # This file
```

## 🔑 Key Technologies

- **Backend**: FastAPI, Motor (MongoDB async driver), PyJWT, Bcrypt
- **Frontend**: React 19, React Router, Axios, Tailwind CSS
- **UI Components**: Shadcn UI, Lucide Icons
- **Real-time**: WebSocket (FastAPI WebSocket + JavaScript WebSocket API)
- **Database**: MongoDB
- **Styling**: Tailwind CSS, Google Fonts (Poppins, Montserrat)

## 📝 API Endpoints

### Authentication
- `POST /api/auth/register` - Register new user
- `POST /api/auth/login` - Login user

### User Management
- `GET /api/user/profile` - Get user profile
- `PUT /api/user/profile` - Update user profile

### Dashboard
- `GET /api/dashboard/stats` - Get dashboard statistics

### Events
- `GET /api/events` - Get all events
- `POST /api/events/{event_id}/register` - Register for event

### Chat/Connect
- `GET /api/users/search?q={query}` - Search users
- `GET /api/messages/{other_user_id}` - Get chat messages
- `POST /api/messages` - Send message
- `WS /ws/{user_id}` - WebSocket connection

### Donations
- `POST /api/donations` - Create donation

### Contact
- `POST /api/feedback` - Submit feedback

## 🎨 Design Features

- Colorful, modern UI with blues, purples, and oranges
- Google Fonts: Poppins (headings), Montserrat (body)
- 20+ high-quality images from Unsplash
- Responsive design for mobile, tablet, and desktop
- Smooth animations and hover effects
- Glass-morphism effects

## 🐛 Troubleshooting

### MongoDB Connection Issues
```bash
# Check if MongoDB is running
sudo systemctl status mongod

# Start MongoDB
sudo systemctl start mongod
```

### Port Already in Use
```bash
# Kill process on port 8001
lsof -ti:8001 | xargs kill -9

# Kill process on port 3000
lsof -ti:3000 | xargs kill -9
```

### WebSocket Connection Failed
- Ensure backend is running on port 8001
- Check that WebSocket URL matches your backend URL
- For Codespaces, ensure WSS (not WS) protocol is used with correct URL

### Codespaces Port Forwarding
- Go to PORTS tab in VS Code
- Ensure ports 3000 and 8001 are both showing "green" status
- If not, restart the services

## 📦 Building for Production

### Backend
```bash
cd backend
pip install -r requirements.txt
uvicorn server:app --host 0.0.0.0 --port 8001
```

### Frontend
```bash
cd frontend
yarn build
```
The build files will be in `frontend/build/` directory.

## 🔒 Security Notes

- Change `JWT_SECRET` in production
- Use environment variables for all sensitive data
- Enable HTTPS in production
- Set proper CORS origins instead of `*`
- Implement rate limiting for production

## 📄 License

This project is open source and available for educational purposes.

## 👥 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📧 Contact

For questions or support, contact: alumni@globalhorizon.edu

---

**Made with ❤️ for Global Horizon University Alumni Network**

- **Events Management**: Browse and register for 10+ upcoming events
- **Real-time Chat**: Connect and chat with alumni using WebSocket
- **Donation Portal**: Support university causes with integrated payment flow
- **Rich About Page**: 1000+ words of university information with image gallery
- **Contact System**: Feedback form with 200-word limit
- **Profile Management**: Edit profile and view activity history
