import React, { useState } from 'react';
import axios from 'axios';

const CreateUserPage = () => {
    const [formData, setFormData] = useState({
        username: '',
        eyeColour: '',
        hairColour: '',
        email: '',
    });

    const [error, setError] = useState('');
    const [success, setSuccess] = useState(false);


const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData({
        ...formData,
        [name]: value
    });
};

const handleSubmit = (e) => {
    e.preventDefault();
    // Adjust the API endpoint based on your Django backend setup
    axios.post('http://127.0.0.1:8000/api/users/', formData)
      .then(response => {
        setSuccess(true);
        setError('');
      })
      .catch(err => {
        setError('Error creating user. Please try again.');
        setSuccess(false);
      });
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
                <div>
                    <label>Email:</label>
                    <input
                        type='email'
                        name='email'
                        value={formData.email}
                        onChange={handleChange}
                        required
                    />
                </div>
                <div>
                    <button type='submit'>Create User</button>
                </div>
            </form>
    </div>
  )
}

export default CreateUserPage;
