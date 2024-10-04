import React from 'react';
import { Link } from 'react-router-dom';
import './Navbar.css'; // Import the CSS file for styles

const Navbar = () => {
    return (
        <nav className="navbar">
            <ul className="navbar-list">
                <li className="navbar-item">
                    <Link to="/">Home</Link>
                </li>
                <li className="navbar-item">
                    <Link to="/login">Login</Link>
                </li>
                <li className="navbar-item">
                    <Link to="/register">Register</Link>
                </li>
                {/* <li className="navbar-item">
                    <Link to="/create-user">Create User</Link>
                </li> */}
                <li className="navbar-item">
                    <Link to="/diary">Diary</Link>
                </li>
                <li className="navbar-item">
                    <Link to="/locker">Locker</Link>
                </li>
            </ul>
        </nav>
    );
};

export default Navbar;