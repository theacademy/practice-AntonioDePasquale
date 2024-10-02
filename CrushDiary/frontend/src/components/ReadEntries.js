import React, { useEffect, useState } from 'react';
import axios from 'axios';

// const ReadEntries = ({ entries }) => {  // Accept entries as props
const ReadEntries = () => {
  const [entries, setEntries] = useState([]);
  const token = localStorage.getItem('token'); // Get token from localStorage

  useEffect(() => {
    const fetchEntries = async () => {
      const response = await axios.get('http://127.0.0.1:8000/api/diary/', {
        headers: { 'Authorization': `Token ${token}` } // Include token in headers
      });
      setEntries(response.data);
    };
    fetchEntries();
  }, [token]);

  return (
    <div className="list-container">
      <h2 className="list-title">Diary Entries</h2>
      <ul className="entry-list">
        {entries.map((entry) => (
          <li className="entry-item" key={entry.entryId}>
            <span className="entry-info"></span>
            <strong>{entry.title} </strong> {entry.createdAt} - {entry.mood} | {entry.updatedAt} 
            <span />
            <span className="entry-content">Dear Diary, {entry.content}</span>
          </li>
        ))}
      </ul>
    </div>
  );
};

export default ReadEntries;