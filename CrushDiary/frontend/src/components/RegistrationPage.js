import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import axios from 'axios';

const RegistrationPage = () => {
    const [email, setEmail] = useState('');
    const [username, setUsername] = useState('');
    const [password, setPassword] = useState('');
    
    // Default values for additional fields
    const [inGameName] = useState('Tony'); // Default value
    const [eyeColour] = useState('Blue'); // Default value
    const [hairColour] = useState('Brown'); // Default value
    
    const [error, setError] = useState('');
    const [success, setSuccess] = useState(false);
    const [loading, setLoading] = useState(false); // Loading state
    const navigate = useNavigate();

    const handleSubmit = async (e) => {
        e.preventDefault();
        setLoading(true); // Start loading

        try {
            const response = await axios.post('http://127.0.0.1:8000/auth/register/', {
                email,
                username,
                password,
                inGameName,
                eyeColour,
                hairColour
            });

            // Handle success response
            setSuccess(true);
            setError(''); // Clear any previous errors
            console.log("Response:", response.data); // Log the response for debugging
            // Clear input fields
            setEmail('');
            setUsername('');
            setPassword('');
        } catch (err) {
            // Handle error response
            const errorMessage = err.response?.data || 'Error creating account. Please try again.';
            setError(typeof errorMessage === 'object' ? JSON.stringify(errorMessage) : errorMessage);
            setSuccess(false);
        } finally {
            setLoading(false); // End loading
        }
    };

    return (
        <div className='registration-page'>
            <hr/>
            <h1>Register</h1>
            <hr/>
            {error && <div className='error'>{error}</div>}
            {success ? (
                <div className='success'>
                    Registration successful! You can now log in with your email: {email}
                    <button onClick={() => navigate('/login')}>Go to Login</button>
                </div>
            ) : (
                <form onSubmit={handleSubmit}>
                    <div>
                        <label>Email:</label>
                        <input
                            type='email'
                            value={email}
                            onChange={(e) => setEmail(e.target.value)}
                            required
                        />
                    </div>
                    <div>
                        <label>Username:</label>
                        <input
                            type='text'
                            value={username}
                            onChange={(e) => setUsername(e.target.value)}
                            required
                        />
                    </div>
                    <div>
                        <label>Password:</label>
                        <input
                            type='password'
                            value={password}
                            onChange={(e) => setPassword(e.target.value)}
                            required
                        />
                    </div>
                    {/* Hidden fields for in-game name, eye colour, and hair colour */}
                    <hr/>
                    <div>
                        <button type='submit' disabled={loading}>
                            {loading ? 'Registering...' : 'Register'}
                        </button>
                    </div>
                </form>
            )}
        </div>
    );
};

export default RegistrationPage;
