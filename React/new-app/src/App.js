import logo from './logo.svg';
import './App.css';
import F2C from './components/Fahrenheit2Celsius';
import C2F from './components/Celsius2Fahrenheit';
import Greetings from './components/Greetings';

function App() {
  return (
    <div className="App">
      <Greetings name="Tony" greeting="Hey dude"/>
      <Greetings name="Nadhia" greeting="Whats up"/>
      <Greetings name="Cindy" greeting="Hello"/>

      <F2C/>

      <C2F/>

    </div>
  );
}

export default App;
