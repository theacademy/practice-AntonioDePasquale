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
        <div className="calculator">
            <Display input={input} />
            <div className="button-container">
                <div className="button-row">
                    <Buttons value="7" onClick={handleButtonClick} />
                    <Buttons value="8" onClick={handleButtonClick} />
                    <Buttons value="9" onClick={handleButtonClick} />
                    <Buttons value="+" onClick={handleButtonClick} />
                </div>
                <div className="button-row">
                    <Buttons value="4" onClick={handleButtonClick} />
                    <Buttons value="5" onClick={handleButtonClick} />
                    <Buttons value="6" onClick={handleButtonClick} />
                    <Buttons value="-" onClick={handleButtonClick} />
                </div>
                <div className="button-row">
                    <Buttons value="1" onClick={handleButtonClick} />
                    <Buttons value="2" onClick={handleButtonClick} />
                    <Buttons value="3" onClick={handleButtonClick} />
                    <Buttons value="*" onClick={handleButtonClick} />
                </div>
                <div className="button-row">
                    <Buttons value="C" onClick={handleButtonClick} />
                    <Buttons value="0" onClick={handleButtonClick} />
                    <Buttons value="=" onClick={handleButtonClick} />
                    <Buttons value="/" onClick={handleButtonClick} />
                </div>
            </div>
        </div>
    );
};


export default Calculator;