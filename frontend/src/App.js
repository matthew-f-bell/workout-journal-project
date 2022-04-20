import logo from './logo.svg';
import './App.css';
import { useState, useEffect } from "react"
import axios from "axios"
import NavBar from './components/navbar';


function App() {

  const[exerciseList, setExerciseList] = useState([])

  useEffect(()=>{
    axios
      .get("/api/exercises")
      .then((res) => {
        console.log(res.data)
        setExerciseList(res.data)
      })
      .catch((err) => console.log(err))
  }, [])

  return (
    <div className="App">
      <NavBar/>
      <div>
        <p> {exerciseList.map((e) => {
          return(
            <div>
              <p> {e.name}</p>
              <p> {e.description}</p>
            </div>
          )
        })} </p>
      </div>
    </div>
  );
}

export default App;
