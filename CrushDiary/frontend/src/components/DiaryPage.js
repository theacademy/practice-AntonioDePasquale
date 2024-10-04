import React, { useEffect, useState } from 'react';
import CreateEntry from './CreateEntry';
import ReadEntries from './ReadEntries';
import DeleteEntry from './DeleteEntry';
import axios from 'axios';
import { useAuth } from './AuthContext';

const DiaryPage = () => {
    const { user, token } = useAuth();
    const [entries, setEntries] = useState([]);
    const [error, setError] = useState(null);
    const [isLoading, setIsLoading] = useState(true);

    const refreshEntries = async () => {
        if (!token) {
            setError('You must be logged in to view entries.');
            setIsLoading(false);
            return;
        }

        try {
            const response = await axios.get('http://127.0.0.1:8000/api/entries/', {
                headers: { 'Authorization': `Token ${token}` },
            });

            console.log('Fetched entries:', response.data);
            setEntries(response.data);
            setError(null);
        } catch (err) {
            console.error('Error fetching entries:', err);
            setError('Failed to load diary entries. Please try again.');
        } finally {
            setIsLoading(false);
        }
    };
    // should i backtrack it to last version
    //no
    //its fine
    // we need to recreate the DB 
    //do it i guess, but make an account before the demo

    useEffect(() => {
        if (user) {
            refreshEntries();
        } else {
            setIsLoading(false);
        }
    }, [user, token]);

    if (isLoading) {
        return <div>Loading...</div>;
    }

    return (
        <div>
            <h1>Your Diary</h1>
            {user ? (
                <>
                    <CreateEntry refreshEntries={refreshEntries} />
                    <ReadEntries entries={entries} error={error} />
                    {/* <DeleteEntry refreshEntries={refreshEntries} /> */}
                </>
            ) : (
                <p>Please log in to view your diary.</p>
            )}
        </div>
    );
};

export default DiaryPage;