import React, { useState } from 'react';
import axios from 'axios';

const CreateEntry = ({ refreshEntries }) => {  // Accept refreshEntries as a prop
    const [title, setTitle] = useState('');
    const [content, setContent] = useState('');
    const [mood, setMood] = useState('Musical');
    const [success, setSuccess] = useState(false);
    const [error, setError] = useState('');

    const handleSubmit = (e) => {
        e.preventDefault();

        axios.post('http://127.0.0.1:8000/api/diary/', {
            title: title,
            content: content,
            mood: mood,
            diaryId: 1  // Make sure to pass the correct diaryId
        })
        .then(response => {
            setSuccess(true);
            setError('');
            refreshEntries();  // Call the function to refresh entries
            // Optionally clear the input fields after submission
            setTitle('');
            setContent('');
            setMood('Musical');
        })
        .catch(err => {
            setError('Error creating Diary Entry. Please try again.');
            setSuccess(false);
        });
    };

    return (
        <div className='entry-form'>
            <h1>Write in your diary!</h1>
            {error && <div className='error'>{error}</div>}
            {success && <div className='success'>Diary entry created successfully!</div>}
            <form onSubmit={handleSubmit}>
                <div className="form-group">
                    <label className="form-label">Title:</label>
                    <input
                        type='text'
                        value={title}
                        onChange={(e) => setTitle(e.target.value)}
                        required
                        className="form-input"
                    />
                </div>
                <div className="form-group">
                    <label className="form-label">Content:</label>
                    <textarea
                        value={content}
                        onChange={(e) => setContent(e.target.value)}
                        required
                        className="form-textarea"
                    />
                </div>
                <div className="form-group">
                    <label className="form-label">Mood:</label>
                    <select
                        value={mood}
                        onChange={(e) => setMood(e.target.value)}
                        required
                        className="form-select"
                    >
                        <option value="Musical">Musical</option>
                        <option value="Sporty">Sporty</option>
                        <option value="Artistic">Artistic</option>
                        <option value="Fashion">Fashion</option>
                        <option value="Nerdy">Nerdy</option>
                    </select>
                </div>
                <div className="form-group">
                    <button type='submit' className="submit-button">Create Entry</button>
                </div>
            </form>
        </div>
    );
};

export default CreateEntry;