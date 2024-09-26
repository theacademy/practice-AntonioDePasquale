import React, { useState } from 'react';
import axios from 'axios';

const AddNewDVD = () => {
    const [dvd, setDvd] = useState({
        title: '',
        releaseYear: '',
        director: '',
        rating: ''
    });

    const handleChange = (e) => {
        setDvd({
            ...dvd,
            [e.target.name]: e.target.value
        });
    };

    const handleSubmit = async (e) => {
        e.preventDefault();
        try {
            await axios.post('http://dvd-library.us-east-1.elasticbeanstalk.com/dvd', dvd);
            alert("DVD added Successfully");
        } catch (error) {
            alert("Error adding DVD");
        }
    };

    return (
        <div>
            <h2>Create New DVD</h2>
            <form onSubmit={handleSubmit}>
                <input
                    type="text"
                    name="title"
                    placeholder="Title"
                    value={dvd.title}
                    onChange={handleChange}
                    required
                />
                <input
                    type="text"
                    name="releaseYear"
                    placeholder="Release Year"
                    value={dvd.releaseYear}
                    onChange={handleChange}
                    required
                />
                <input
                    type="text"
                    name="director"
                    placeholder="Director"
                    value={dvd.director}
                    onChange={handleChange}
                    required
                />
                <input
                    type="text"
                    name="rating"
                    placeholder="Rating"
                    value={dvd.rating}
                    onChange={handleChange}
                    required
                />
                <button type="submit">Add new DVD</button>
            </form>
        </div>
    );
};

export default AddNewDVD;