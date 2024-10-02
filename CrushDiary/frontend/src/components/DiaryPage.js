// pages/DiaryPage.js
import React, { useEffect, useState } from 'react';
import CreateEntry from './CreateEntry';
import ReadEntries from './ReadEntries';
import DeleteEntry from './DeleteEntry';
import axios from 'axios';

const DiaryPage = () => {
  const [entries, setEntries] = useState([]);

  const fetchEntries = async () => {
    try {
      const response = await axios.get('http://127.0.0.1:8000/api/diary/');
      setEntries(response.data);
    } catch (error) {
      console.error('Error fetching entries:', error);
    }
  };

  useEffect(() => {
    fetchEntries();
  }, []);

  return (
    <div>
      <h1>Your Diary</h1>
      <CreateEntry refreshEntries={fetchEntries} />
      <ReadEntries entries={entries} />
      <DeleteEntry refreshEntries={fetchEntries} />
    </div>
  );
};

export default DiaryPage;