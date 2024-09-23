import React, { Component } from "react";

class CounterClass extends Component {
    constructor(props) {
        super(props);
        this.state = {
            counter: 0
        };
    }

    addOne = () => {
        this.setState((prevState) => ({
            counter: prevState.counter + 1
        }));
    }

    subOne = () => {
        this.setState((prevState) => ({
            counter: prevState.counter - 1
        }));
    }

    render() {
        return (
            <div>
                <h2>My Counter</h2>
                <p>Counter: {this.state.counter}</p>
                <input type='button' onClick={this.addOne} value='Add 1' />
                <br />
                <input type='button' onClick={this.subOne} value='Subtract 1' />
            </div>
        );
    }
}

export default CounterClass;
