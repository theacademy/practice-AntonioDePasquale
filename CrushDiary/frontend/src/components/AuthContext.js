import React, { createContext, useContext, useState } from 'react';

const AuthContext = createContext();

export const AuthProvider = ({ children }) => {
    const [userEmail, setUserEmail] = useState('');
    const [token, setToken] = useState({
        user_id: 3,
        email: "anton@gmail.com",
        
    });

    return (
        <AuthContext.Provider value={{ userEmail, setUserEmail, token, setToken }}>
            {children}
        </AuthContext.Provider>
    );
};

export const useAuth = () => useContext(AuthContext);