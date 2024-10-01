import React, { useEffect, useState } from 'react';
import axios from 'axios';

const ReadEntries = () => {
  const [entries, setEntries] = useState([]);

  useEffect(() => {
    const fetchEntries = async () => {
      const response = await axios.get('http://127.0.0.1:8000/api/diary/');
      setEntries(response.data);
    };
    fetchEntries();
  }, []);

  return (
    <div className="list-container">
      <h2 className="list-title">Diary Entries</h2>
      <ul className ="entry-list">
        {entries.map((entry) => (
          <li className="entry-item" key={entry.entryId}>
            <span className="entry-info"></span>
            <strong>{entry.title} </strong>  {entry.createdAt} - {entry.mood} | {entry.updatedAt} 
            <span/> 
            <span className="entry-content"> Dear Diary, {entry.content} </span>
          </li>
        ))}
      </ul>
    </div>
  );
};

// {entry.diaryId} 
// {entry.title}c
// {entry.content} 
// {entry.mood}
// {entry.createdAt}
// {entry.updatedAt} 

// entryId 
// diaryId 
// title 
// content 
// mood 
// createdAt
// updatedAt 
export default ReadEntries;