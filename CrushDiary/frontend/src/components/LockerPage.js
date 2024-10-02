// pages/LockerPage.js
import React from 'react';
import { Link } from 'react-router-dom';
import ReadMemosComp from './ReadMemos';
// import './App.css'; 

const LockerPage = () => {
  return (
    <div className="locker-page">
      <h2>Inside Your Locker Page</h2>
      <hr/>
      <ReadMemosComp/>
      <hr/>
      <Link to="/diary">Go to Diary</Link>
    </div>
  );
}

export default LockerPage;