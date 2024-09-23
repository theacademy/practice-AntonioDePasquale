import React from 'react';

const Buttons = ({ value, onClick }) => {
    return (
        <button onClick={() => onClick(value)}>
            {value}
        </button>
    );
};

export default Buttons;