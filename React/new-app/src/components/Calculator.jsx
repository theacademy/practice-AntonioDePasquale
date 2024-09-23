import React, { useState } from 'react';
import Display from './CalculatorDisplay';
import Buttons from './CalculatorButtons';

const Calculator = () => {
    const [input, setInput] = useState('');

    const handleButtonClick = (value) => {
        if (value === '=') {
            try {
                setInput(eval(input).toString())
            } catch (error) {
                setInput('Error');
            }
        } else if (value === 'C') {
            setInput('');
        } else {
            setInput(input + value);
        }
    };

    return (
        <div>
            <Display input={input} />
            <div>
                {['1', '2', '3', '+', 'C', '4', '5', '6', '-', '=', '7', '8', '9', '*', '0', '/'].map((item) => (
                    <Buttons key={item} value={item} onClick={handleButtonClick} />
                ))}
            </div>
        </div>
    );
};

export default Calculator;