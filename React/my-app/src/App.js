// import logo from './logo.svg';
// import './App.css';
import React from'react';
import MyTimer from './components/Timer';
import MyStopwatch from './components/Stopwatch';
import MyTime from './components/Time';

function App() {

  // const time = new Date();
  // time.setSeconds(time.getSeconds() + 600); // 10 minutes timer

  return (
    <div className="App">
      <MyTimer/>
      <hr/>
      <MyStopwatch/>
      <hr/>
      <MyTime/>
      <hr/>

    </div>
  );
}

export default App;
