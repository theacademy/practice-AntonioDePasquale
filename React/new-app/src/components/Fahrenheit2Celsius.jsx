import React, { useState } from "react";

function F2C() {
    const [fahrenheit, setFahrenheit] = useState('');
    const [celsius, setCelsius] = useState('');

    const convertToCelsius = (f) => {
        return (f -32) * 5 / 9;
    }

    const handleChange = (e) => {
        const f = e.target.value
        setFahrenheit(f);
        setCelsius(convertToCelsius(f).toFixed(2));
    }

    return (
        <div>
            <h2>Fahrenheit to Celsius</h2>
            <label>Fahrenheit: </label>
            <input
                type="number"
                value={fahrenheit}
                onChange={handleChange}
                placeholder="Enter Fahrenheit" />
                <p>{fahrenheit}&deg;F is {celsius}C&deg;</p>
        </div>
    )
}

export default F2C;