import React, { useEffect, useState } from 'react';
import axios from 'axios';

const ReadMemos = () => {
  const [memos, setMemos] = useState([]);
  const token = localStorage.getItem('token'); // Get token from localStorage


  useEffect(() => {
    const fetchMemos = async () => {
        const response = await axios.get('http://127.0.0.1:8000/api/locker/', {
          headers: { 'Authorization': `Token ${token}` } // Include token in headers
        });
        setMemos(response.data);
      };
      fetchMemos();
    }, [token]);

  return (
    <div className="memo-container">
      <h2 className="memo-title">Love Notes</h2>
      <ul className ="memo-list">
        {memos.map((memo) => (
          <li className="memo-item" key={memo.memoId}>
            <span className="memo-info"></span>
            <strong>{memo.title} </strong> 
            <span/> 
            <span className="memo-content"> {memo.content} </span>
          </li>
        ))}
      </ul>
    </div>
  );
};

export default ReadMemos;