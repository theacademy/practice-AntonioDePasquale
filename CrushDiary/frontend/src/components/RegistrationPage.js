import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';

const RegistrationPage = () => {
    const [email, setEmail] = useState('');
    const [password, setPassword] = useState('');
    const navigate = useNavigate();

    const handleSubmit = async (e) => {
        e.preventDefault();

        try {
            const response = await fetch("http://127.0.0.1:8000/api/signInDetail/", {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ username: email, password: password }),
            });

            if (!response.ok) {
                throw new Error("Registration Failed");
            }

            const data = await response.json();
            // localStorage.setItem('token', data.token);

            navigate('/diary');
        } catch (err) {
            console.error('Registration error:', err);
        }
    }

    return (
        <div>
            <h1>Registration Page</h1>
            <form onSubmit={handleSubmit}>
                <label>
                    Email:
                    <input 
                        type="email"
                        value={email}
                        onChange={(e) => setEmail(e.target.value)}
                        required
                    />
                </label>
                <br />
                <label>
                    Password:
                    <input 
                        type="password"
                        value={password}
                        onChange={(e) => setPassword(e.target.value)}
                        required
                    />
                </label>
                <br />
                <input type="submit" value="Register" />
            </form>
            <p>Already have an account? <a href="/login">Login</a></p>
        </div>
    )
}

export default RegistrationPage;