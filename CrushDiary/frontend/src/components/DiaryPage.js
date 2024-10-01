// pages/DiaryPage.js
import React from 'react';
import { Link } from 'react-router-dom';
import DeleteEntryComp from './DeleteEntry';
import ReadEntriesComp from './ReadEntries';

const DiaryPage = () => {
  return (
    <div>
      <h2>Diary Page</h2>
      <ReadEntriesComp/>
      <hr/>
      <DeleteEntryComp/>
      <hr/>
      <Link to="/locker">Go to Locker</Link>
    </div>
  );
}

export default DiaryPage;