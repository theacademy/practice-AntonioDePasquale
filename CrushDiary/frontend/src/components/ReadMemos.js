import React, { useEffect, useState } from 'react';
import axios from 'axios';
import { useAuth } from './AuthContext';

const ReadMemos = () => {
  const [memos, setMemos] = useState([]);
  // const token = localStorage.getItem('token'); // Get token from localStorage
  const { token, user } = useAuth(); 

  useEffect(() => {
    const fetchMemos = async () => {
        const response = await axios.get('http://127.0.0.1:8000/api/memos/'
          // , {headers: { 'Authorization': `Token ${token}` }}
        );
        setMemos(response.data);
      };
      fetchMemos();
    }, 
    // [token]);
    []);


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