import React from 'react';
import { BrowserRouter as Router, Route, Routes, Link } from 'react-router-dom';
import LoginPage from './components/LoginPage';
import RegistrationPage from './components/RegistrationPage';
import CreateUserPage from './components/CreateUserPage';
import DiaryPage from './components/DiaryPage';
import LockerPage from './components/LockerPage';
import { AuthProvider } from './components/AuthContext';
import './App.css';
import Navbar from './components/NavFolder/NavbarComp';



function App() {
  return (
    <AuthProvider>
      <Router>
        <div className="page-container">
          <Navbar />
          <div className="content-wrapper">
            <Routes>
              <Route path="/" element={
                <div className="home-container">
                  <h1>Welcome to the Crush Diary</h1>
                  <div className="character-container">
                    <img src="anime-girl.jpg" alt="Animated character" className="animated-character" />
                  </div>
                  <div className="home-buttons">
                    {/* <Link to="/register">
                    <button>Register</button>
                    </Link> */}
                    <Link to="/login">
                    <button>Login</button>
                    </Link>
                  </div>
                  {/* <h2>Write in your diary...your dreams may actually come true!</h2> */}
                </div>
              } />
              <Route path="/" exact element={<h2>Write in your diary...your dreams may actually come true!</h2>} />
              <Route path="/login" element={<LoginPage />} />
              <Route path="/register" element={<RegistrationPage />} />
              <Route path="/create-user" element={<CreateUserPage />} />
              <Route path="/diary" element={<DiaryPage />} />
              <Route path="/locker" element={<LockerPage />} />
            </Routes>
          </div>
        </div>
      </Router>
    </AuthProvider>
  );
}

export default App;
