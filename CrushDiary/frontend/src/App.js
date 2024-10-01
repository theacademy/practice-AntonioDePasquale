import React from 'react';
import { BrowserRouter as Router, Route, Routes, Link } from 'react-router-dom';
import LoginPage from './components/LoginPage';
import RegistrationPage from './components/RegistrationPage';
import CreateUserPage from './components/CreateUserPage';
import DiaryPage from './components/DiaryPage';
import LockerPage from './components/LockerPage';

function App() {
  return (
    <Router>
      <nav>
        <ul>
          <li>
            <Link to="/">Home</Link>
          </li>
          <li>
            <Link to="/login">Login</Link>
          </li>
          <li>
            <Link to="/register">Register</Link>
          </li>
          <li>
            <Link to="/create-user">Create User</Link>
          </li>
          <li>
            <Link to="/diary">Diary</Link>
          </li>
          <li>
            <Link to="/locker">Locker</Link>
          </li>
        </ul>
      </nav>

      <Routes>
        <Route path="/" exact element={<h1>Welcome to the Diary App!</h1>} />
        <Route path="/login" element={<LoginPage />} />
        <Route path="/register" element={<RegistrationPage />} />
        <Route path="/create-user" element={<CreateUserPage />} />
        <Route path="/diary" element={<DiaryPage />} />
        <Route path="/locker" element={<LockerPage />} />
      </Routes>
    </Router>
  );
}

export default App;
