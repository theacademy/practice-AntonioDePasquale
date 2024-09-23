import React from 'react';

function Child({num1, num2}) {
    const product = num1 * num2

    return (
        <>
            <p>The Product of {num1} and {num2} is : {product}</p>
        </>
    );
}

export default Child;
