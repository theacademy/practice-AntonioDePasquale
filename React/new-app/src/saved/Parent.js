import React from 'react';
import Child from './Child';

function Parent() {
    const num1 = 20
    const num2 = 50

    return (
        <>
            <h1>The Product of two numbers, {num1} and {num2} is : {num1 * num2}</h1>
            <Child num1={num1} num2={num2} />
        </>
    )
}

export default Parent;