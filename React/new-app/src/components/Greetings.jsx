import React from "react";

function Greetings(props) {
    return (
        <div>
            <h2>{props.greeting}, {props.name}!</h2>
        </div>
    );
}

export default Greetings;