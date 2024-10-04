// import React, { useEffect, useState } from 'react';
// import axios from 'axios';
// import { useAuth } from './AuthContext';

// // const ReadEntries = ({ entries }) => {  // Accept entries as props
// const ReadEntries = () => {
//   console.log('Reading entries...');
//   const [entries, setEntries] = useState([]);
//   const { token, user } = useAuth(); 
//   // const token = localStorage.getItem('token'); // Get token from localStorage
//   const [error, setError] = useState(null);

//   useEffect(() => {
//   //   const fetchEntries = async () => {
//   //     const response = await axios.get('http://127.0.0.1:8000/api/entries/', 
//   //       // {headers: { 'Authorization': `Token ${token}` } // Include token in headers}
//   //   );
//   //     setEntries(response.data);
//   //   };
//   //   fetchEntries();
//   // }, [token]);

//     const fetchEntries = async () => {
//     // if (!token) {
//     //   setError('You must be logged in to view entries.');
//     //   return;
//     // }
    
//       try {
//         const response = await axios.get('http://127.0.0.1:8000/api/entries/'
//           // , { headers: { 'Authorization': `Token ${token}` } }
//       );
//         setEntries(response.data);
//       } catch (err) {
//         console.error('Error fetching entries:', err);
//         setError('Failed to load diary entries. Please try again.');
//       }
//   };

//   fetchEntries();
// // }, [token]);
// }, []); 

// //   return (
// //     <div className="list-container">
// //       <h2 className="list-title">Diary Entries</h2>
// //       <ul className="entry-list">
// //         {entries.map((entry) => (
// //           <li className="entry-item" key={entry.entryId}>
// //             <span className="entry-info"></span>
// //             <strong>{entry.title} </strong> {entry.createdAt} - {entry.mood} | {entry.updatedAt} 
// //             <span />
// //             <span className="entry-content">Dear Diary, {entry.content}</span>
// //           </li>
// //         ))}
// //       </ul>
// //     </div>
// //   );
// // };

// return (
//   <div className="list-container">
//     <h2 className="list-title">Diary Entries</h2>
//     {error ? <p style={{ color: 'red' }}>{error}</p> : null}
//     <ul className="entry-list">
//       {entries.length > 0 ? (
//         entries.map((entry) => (
//           <li className="entry-item" key={entry.entryId}>
//             <strong> {entry.title}</strong> {entry.createdAt} {entry.mood}  {entry.updatedAt}
//             <p className="entry-content">Dear Diary, {entry.content}</p>
//           </li>
//         ))
//       ) : (
//         <p>No diary entries found.</p>
//       )}
//     </ul>
//   </div>
// );
// };

// export default ReadEntries;

import React, { useEffect, useState } from 'react';
import axios from 'axios';
import { useAuth } from './AuthContext';

const ReadEntries = ({ refreshEntries }) => { // Accept refreshEntries as a prop
  const [entries, setEntries] = useState([]);
  const { token } = useAuth(); 
  const [error, setError] = useState(null);

  const fetchEntries = async () => {
    if (!token) {
      setError('You must be logged in to view entries.');
      return;
    }

    try {
      const response = await axios.get('http://127.0.0.1:8000/api/entries/', {
        headers: { 'Authorization': `Token ${token}` }, // Include token in headers
      });
      setEntries(response.data);
    } catch (err) {
      console.error('Error fetching entries:', err);
      setError('Failed to load diary entries. Please try again.');
    }
  };

  useEffect(() => {
    fetchEntries();
  }, [token]);

  return (
    <div className="list-container">
      <h2 className="list-title">Diary Entries</h2>
      {error && <p style={{ color: 'red' }}>{error}</p>}
      <ul className="entry-list">
        {entries.length > 0 ? (
          entries.map((entry) => (
            <li className="entry-item" key={entry.entryId}>
              <strong>{entry.title}</strong> {entry.createdAt} {entry.mood} {entry.updatedAt}
              <p className="entry-content">Dear Diary, {entry.content}</p>
            </li>
          ))
        ) : (
          <p>No diary entries found.</p>
        )}
      </ul>
    </div>
  );
};

export default ReadEntries;
