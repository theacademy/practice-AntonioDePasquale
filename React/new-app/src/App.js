import logo from './logo.svg';
import './App.css';
import React from 'react';
import Calculator from './components/Calculator';
// import F2C from './saved/Fahrenheit2Celsius';
// import C2F from './saved/Celsius2Fahrenheit';
// import Greetings from './saved/Greetings';
// import Counter from './saved/Counter';
// import Parent from './saved/Parent';
// import { smallButton, bigButton } from './saved/Buttons'; // Corrected import

// function App() {
//   return (
//     <div className="App">
//       <Greetings name="Tony" greeting="Hey dude"/>
//       <Greetings name="Nadhia" greeting="Whats up"/>
//       <Greetings name="Cindy" greeting="Hello"/>

//       <F2C/>

//       <C2F/>

//     </div>
//   );
// }

// function App() {
//   return (
//     <div className="App">
//       {/* <Counter/> */}
//       <Parent/>
//     </div>
//   );
// }

// function App() {
//   return (
//     <div className="App">
//       {smallButton()}
//       {bigButton()}
//     </div>
//   );
// }

function App() {
  return (
    <div className="App">
      <Calculator/>
    </div>
  );
}

export default App;
