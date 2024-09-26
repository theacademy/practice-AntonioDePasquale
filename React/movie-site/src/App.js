//import './App.css';
import ListDVDs from "./components/DVDList";
import AddNewDVD from "./components/AddDVD";
import DeleteDVD from "./components/DeleteDVD";

function App() {
  return (
    <div className="App">
      <h1>DVD List</h1>
      <ListDVDs />
      <hr/>
      <h2>create dvd listing</h2>
      <AddNewDVD />
      <h2>delete dvd listing</h2>
      <DeleteDVD />

    </div>
  );
}

export default App;
