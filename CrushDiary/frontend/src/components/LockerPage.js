// pages/LockerPage.js
import React from 'react';
import { Link } from 'react-router-dom';

const LockerPage = () => {
  return (
    <div>
      <h2>Locker Page</h2>
      <Link to="/diary">Go to Diary</Link>
    </div>
  );
}

export default LockerPage;