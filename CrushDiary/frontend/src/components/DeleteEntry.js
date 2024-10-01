import React, { useState } from 'react';
import axios from 'axios';


const DeleteEntry = () => {
  const [id, setId] = useState('');
  
  const handleDelete = async (e) => {
    e.preventDefault();
    try {
      await axios.delete(`http://127.0.0.1:8000/api/diary/${id}`);
      console.log('Data deleted');
    } catch (error) {
      console.error('Error deleting data:', error);
    }
  };

  return (
    <form>
    <input
      type="text"
      placeholder="Id"
      value={id}
      onChange={(e) => setId(e.target.value)}
    />
    <button onClick={handleDelete}>Delete Entry</button>
    </form>
  );
};

export default DeleteEntry;