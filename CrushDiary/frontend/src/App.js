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
        <Navbar/>
        <div className="home-container" style={{ textAlign: 'center', marginTop: '20%' }}>
          <h1>Welcome to the Crush Diary</h1>
          <Link to="/register">
            <button style={{ padding: '10px 20px', fontSize: '18px', margin: '10px' }}>Register</button>
          </Link>
          <Link to="/login">
            <button style={{ padding: '10px 20px', fontSize: '18px', margin: '10px' }}>Login</button>
          </Link>
        </div>

        <Routes>
          <Route path="/" exact element={<h2>Write in your diary...your dreams may actually come true!</h2>} />
          <Route path="/login" element={<LoginPage />} />
          <Route path="/register" element={<RegistrationPage />} />
          <Route path="/create-user" element={<CreateUserPage />} />
          <Route path="/diary" element={<DiaryPage />} />
          <Route path="/locker" element={<LockerPage />} />
        </Routes>
      </Router>
    </AuthProvider>
  );
}

export default App;
