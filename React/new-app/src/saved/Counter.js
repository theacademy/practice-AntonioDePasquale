import React, { useState} from "react";

function Counter() {
    const [counter, setCounter] = useState(0)

    const addOne = () => {
        setCounter(counter + 1)
    }

    const subOne = () => {
        setCounter(counter - 1)
    }

    return (
        <div>
            <h2>My Counter</h2>
            <p>Counter: {counter}</p>
            <input type='button' onClick={addOne} value='Add 1'/>
            <br></br>
            <input type='button' onClick={subOne} value='Subtract 1'/>
        </div>
    )
}

export default Counter