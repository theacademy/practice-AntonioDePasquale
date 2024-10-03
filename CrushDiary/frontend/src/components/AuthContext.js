// // AuthContext.js

// AuthContext.js
// import React, { createContext, useContext, useEffect, useState } from 'react';
// import axios from 'axios';

// const AuthContext = createContext();

// export const useAuth = () => {
//     return useContext(AuthContext);
// };

// export const AuthProvider = ({ children }) => {
//     const [user, setUser] = useState(null);
//     const [token, setToken] = useState(localStorage.getItem('token'));
//     const [diaryId, setDiaryId] = useState(localStorage.getItem('diaryId'));  // Store diaryId

//     useEffect(() => {
//         if (token) {
//             axios.defaults.headers.common['Authorization'] = `Token ${token}`;
//             fetchUser();
//         } else {
//             delete axios.defaults.headers.common['Authorization'];
//         }
//     }, [token]);

//     const fetchUser = async () => {
//         try {
//             const response = await axios.get('http://127.0.0.1:8000/api/users/');
//             setUser(response.data);
//         } catch (err) {
//             console.error('Failed to fetch user:', err);
//             setUser(null);
//         }
//     };

//     const login = async (identifier, password) => {
//         try {
//             const response = await axios.post('http://127.0.0.1:8000/auth/login/', { 
//                 identifier, 
//                 password 
//             });
            
//             setToken(response.data.token);
//             localStorage.setItem('token', response.data.token);
    
//             // Log the token after setting it
//             console.log('Token after login:', response.data.token);
    
//             // Store diaryId in state and localStorage
//             setDiaryId(response.data.diaryId);
//             localStorage.setItem('diaryId', response.data.diaryId);
    
//             // Store additional information in the state
//             setUser({
//                 id: response.data.userId,
//                 email: response.data.email,
//                 diaryId: response.data.diaryId,
//                 playerCharacterId: response.data.playerCharacterId,
//                 lockerId: response.data.lockerId,
//             });
//         } catch (err) {
//             console.error('Login failed:', err);
//             throw err;  // Handle this with a notification in the UI
//         }
//     };
    

//     const logout = () => {
//         setToken(null);
//         setUser(null);
//         setDiaryId(null);
//         localStorage.removeItem('token');
//         localStorage.removeItem('diaryId');  // Clear diaryId on logout
//     };

//     return (
//         <AuthContext.Provider value={{ user, token, diaryId, login, logout }}>
//             {children}
//         </AuthContext.Provider>
//     );
// };

import React, { createContext, useContext, useEffect, useState } from 'react';
import axios from 'axios';

const AuthContext = createContext();

export const useAuth = () => {
    return useContext(AuthContext);
};

export const AuthProvider = ({ children }) => {
    const [user, setUser] = useState(null);
    const [token, setToken] = useState(localStorage.getItem('token'));
    
    useEffect(() => {
        if (token) {
            axios.defaults.headers.common['Authorization'] = `Token ${token}`;
            fetchUser();
        } else {
            delete axios.defaults.headers.common['Authorization'];
        }
    }, [token]);

    const fetchUser = async () => {
        try {
            const response = await axios.get('http://127.0.0.1:8000/api/users/');
            setUser(response.data);
        } catch (err) {
            console.error('Failed to fetch user:', err);
            setUser(null);
        }
    };

    const login = async (identifier, password) => {
        console.log('Attempting login with:', { identifier, password }); // Log the data you're sending

        try {
            const response = await axios.post('http://127.0.0.1:8000/auth/login/', { 
                identifier, 
                password 
            });
            
            console.log('Login successful! Response:', response.data); // Log the entire response on success
            console.log('Token:', response.data.token); // Log the token

            setToken(response.data.token);
            localStorage.setItem('token', response.data.token);

            setUser({
                id: response.data.userId,
                email: response.data.email,
                diaryId: response.data.diaryId,
                // Add other user data if needed
            });
        } catch (err) {
            console.error('Login failed:', err); // Log error on failure
            throw err; // Handle UI notification if needed
        }
    };

    const logout = () => {
        setToken(null);
        setUser(null);
        localStorage.removeItem('token');
    };

    return (
        <AuthContext.Provider value={{ user, token, login, logout }}>
            {children}
        </AuthContext.Provider>
    );
};
