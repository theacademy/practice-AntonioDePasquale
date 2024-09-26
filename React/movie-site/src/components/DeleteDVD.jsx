import React, { useState } from 'react';
import axios from 'axios';

const DeleteDVD = () => {
  const [dvdId, setDVDId] = useState('');

  const handleDelete = async (e) => {
    e.preventDefault(); // Prevent default form submission
    try {
      await axios.delete(`http://dvd-library.us-east-1.elasticbeanstalk.com/dvd/${dvdId}`);
      console.log('DVD deleted');
      alert('DVD deleted successfully');
    } catch (error) {
      console.error('Error deleting DVD data:', error);
      alert('Failed to delete DVD');
    }
  };

  return (
    <form onSubmit={handleDelete}>
      <input
        type="text"
        placeholder="DVD ID"
        value={dvdId}
        onChange={(e) => setDVDId(e.target.value)}
        required
      />
      <button type="submit">Delete</button>
    </form>
  );
};

export default DeleteDVD;
