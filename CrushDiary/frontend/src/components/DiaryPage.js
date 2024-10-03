// pages/DiaryPage.js
import React, { useEffect, useState } from 'react';
import CreateEntry from './CreateEntry';
import ReadEntries from './ReadEntries';
import DeleteEntry from './DeleteEntry';
import axios from 'axios';
import { useAuth } from './AuthContext';

const DiaryPage = () => {
  const [entries, setEntries] = useState([]);
  const { token, user } = useAuth();
  const DT=token.diaryId
  const [error, setError] = useState(null);


  useEffect(() => {
    fetchEntries();
  }, []);

  const fetchEntries = async () => {
    const response = await axios.get('http://127.0.0.1:8000/api/entries/')
    setEntries(response.data);
    console.log("Data entries for the logged user: ", user , "data" ,  response.data);
  };

  

  return (
    <div>
      <h1>Your Diary</h1>
      <CreateEntry refreshEntries={fetchEntries} />
      <ReadEntries entries={entries} />
      <DeleteEntry refreshEntries={fetchEntries} />
      {/* <CreateEntry/>
      <ReadEntries/>
      <DeleteEntry/> */}
    </div>
  );
};

export default DiaryPage;