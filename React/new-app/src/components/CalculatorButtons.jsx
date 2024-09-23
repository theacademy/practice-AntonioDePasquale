import React from 'react';

const Buttons = ({ value, onClick }) => {
    return ( 
        <div className="button-wrapper">
            <button onClick={() => onClick(value)}>
                {value}
            </button>
        </div>
    );
};

export default Buttons;