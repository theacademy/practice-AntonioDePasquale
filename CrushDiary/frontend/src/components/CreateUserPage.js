import React, { useState, useEffect } from 'react';
import axios from 'axios';
import { useAuth } from './AuthContext';

const CreateUserPage = () => {
    const { token } = useAuth();  // Get the logged-in user's email

    const [formData, setFormData] = useState({
        user_id: token.user_id,
        username: '',
        eyeColour: '',
        hairColour: '',
        email: token.email,
        //email: userEmail, // This will be populated behind the scenes
    });

    const [error, setError] = useState('');
    const [success, setSuccess] = useState(false);

    const handleChange = (e) => {
        const { name, value } = e.target;
        setFormData({
            ...formData,
            user_id: token.user_id,
            email: token.email,
            [name]: value,
        });
    };

    const handleSubmit = async (e) => {
        e.preventDefault();
        try {
            await axios.put('http://127.0.0.1:8000/api/users/', {
                user_id: token.user_id,
                username: formData.username,
                eyeColour: formData.eyeColour,
                hairColour: formData.hairColour,
                //email: userEmail // Include the email in the request body
                email: token.email // formData.email
            });
            setSuccess(true);
            setError('');
        } catch (err) {
            setError('Error creating user. Please try again.');
            setSuccess(false);
        }
    };

    return (
        <div className='create-user-page'>
            <h1>Create User</h1>
            {error && <div className='error'>{error}</div>}
            {success && <div className='success'>User created successfully!</div>}
            <form onSubmit={handleSubmit}>
                <div>
                    <label>Username:</label>
                    <input
                        type='text'
                        name='username'
                        value={formData.username}
                        onChange={handleChange}
                        required
                    />
                </div>
                <div>
                    <label>Eye Colour:</label>
                    <input
                        type='text'
                        name='eyeColour'
                        value={formData.eyeColour}
                        onChange={handleChange}
                        required
                    />
                </div>
                <div>
                    <label>Hair Colour:</label>
                    <input
                        type='text'
                        name='hairColour'
                        value={formData.hairColour}
                        onChange={handleChange}
                        required
                    />
                </div>
                {/* <div>
                    <label>Email:</label>
                    <input
                        type="email"
                        name="email"
                        //value={userEmail}
                        value={formData.email}
                        onChange={handleChange}
                        //readOnly
                    />
                </div> */}
                <div>
                    <button type='submit'>Create User</button>
                </div>
            </form>
        </div>
    );
};

export default CreateUserPage;


