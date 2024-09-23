import React, { useState } from "react";

function C2F() {
    const [fahrenheit, setFahrenheit] = useState('');
    const [celsius, setCelsius] = useState('');

    const convertToFahrenheit = (c) => {
        return (c * 1.8) + 32
    }

    const handleChange = (e) => {
        const c = e.target.value
        setCelsius(c);
        setFahrenheit(convertToFahrenheit(c).toFixed(2));
    }

    return (
        <div>
            <h2>Celsius to Fahrenheit</h2>
            <label>Celsius: </label>
            <input
                type="number"
                value={celsius}
                onChange={handleChange}
                placeholder="Enter Celsius" />
                <p>{celsius}&deg;C is {fahrenheit}F&deg;</p>
        </div>
    )
}

export default C2F;