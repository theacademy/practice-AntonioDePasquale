import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import { useAuth } from './AuthContext';  // Import the AuthContext
// import './App.css';

const LoginPage = () => {
    const [email, setEmail] = useState('');
    const [password, setPassword] = useState('');
    const navigate = useNavigate();
    const { setUserEmail, setToken } = useAuth();  // Get the context methods
    const [error, setError] = useState('');

    const handleSubmit = async (e) => {
        e.preventDefault();
    
        try {
            const response = await fetch("http://127.0.0.1:8000/auth/login/", {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ email: email, password: password }), // Ensure keys match
            });
    
            if (!response.ok) {
                throw new Error("Login Failed");
            }
    
            const data = await response.json();
            localStorage.setItem('token', data.token);
    
            navigate('/diary');
        } catch (err) {
            console.error('Login error:', err);
        }
    };

    return (
        <div className="login-page">
            <form onSubmit={handleSubmit} className="login-form">
                <h1>Login Page</h1>
                {error && <p style={{ color: 'red' }}>{error}</p>}
                
                <label htmlFor="email">Email:</label>
                <input 
                    type="email" 
                    id="email"
                    value={email} 
                    onChange={(e) => setEmail(e.target.value)} 
                    required 
                />
                
                <label htmlFor="password">Password:</label>
                <input 
                    type="password" 
                    id="password"
                    value={password} 
                    onChange={(e) => setPassword(e.target.value)} 
                    required 
                />
                
                <input type="submit" value="Login" />
                
                <p>Don't have an account? <a href="/register">Register</a></p>
            </form>
        </div>
    );
};

export default LoginPage;

// import React, {useState} from 'react';
// import { useNavigate } from 'react-router-dom';

// const LoginPage = () => {
//     const [email, setEmail] = useState('');
//     const [password, setPassword] = useState('');
//     const navigate = useNavigate();

//     const handleSubmit = async (e) => {
//         e.preventDefault();

//         try {
//             const response = await fetch("http://127.0.0.1:8000/auth/login/", {
//                 method: 'POST',
//                 headers: {
//                     'Content-Type': 'application/json',
//                 },
//                 body: JSON.stringify({ username: email, password: password }),
//             });

//             if (!response.ok) {
//                 throw new Error("Login Failed")
//             }

//             const data = await response.json();
//             localStorage.setItem('token', data.token);

//             navigate('/diary');
//         } catch (err) {
//             console.error('Login error:', err);
//         }
//     }

//     return (
//         <div>
//             <h1>Login Page</h1>
//             <form onSubmit={handleSubmit}>
//                 <label>
//                     Email:
//                     <input 
//                         type="email" 
//                         value={email} 
//                         onChange={(e) => setEmail(e.target.value)} 
//                         required 
//                     />
//                 </label>
//                 <br />
//                 <label>
//                     Password:
//                     <input 
//                         type="password" 
//                         value={password} 
//                         onChange={(e) => setPassword(e.target.value)} 
//                         required 
//                     />
//                 </label>
//                 <br />
//                 <input type="submit" value="Login"/>
//             </form>
//             <p>Don't have an account? <a href="/register">Register</a></p>
//         </div>
//     )
// }

// export default LoginPage;