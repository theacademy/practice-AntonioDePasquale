import React, { useState, useEffect } from 'react';
import axios from 'axios';

const CreateUserPage = () => {
    const [formData, setFormData] = useState({
        username: '',
        eyeColour: '',
        hairColour: '',
    });

    const [error, setError] = useState('');
    const [success, setSuccess] = useState(false);

    useEffect(() => {
        // Fetch the SignInDetail for the logged-in user
        const fetchSignInDetail = async () => {
            try {
                const response = await axios.get('http://127.0.0.1:8000/api/users/'); // Adjust the URL based on your API
                setFormData((prev) => ({ ...prev, email: response.data.email }));
            } catch (err) {
                console.error(err);
                setError('Error fetching user details.');
            }
        };
        fetchSignInDetail();
    }, []);

    const handleChange = (e) => {
        const { name, value } = e.target;
        setFormData({
            ...formData,
            [name]: value
        });
    };

    const handleSubmit = async (e) => {
        e.preventDefault();
        try {
            await axios.post('http://127.0.0.1:8000/api/users/', {
                ...formData,
                email: formData.email // Include the email in the request body
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
                {/* No email input required */}
                <div>
                    <button type='submit'>Create User</button>
                </div>
            </form>
        </div>
    );
};

export default CreateUserPage;

