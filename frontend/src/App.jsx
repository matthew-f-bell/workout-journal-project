import { useState, useEffect } from "react"
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom'
import axios from "axios"
import NavBar from './components/navbar';
import SignUp from "./components/signup";


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
      {/* <NavBar/>
      <SignUp />
      <div>
        <p> {exerciseList.map((e) => {
          return(
            <div>
              <p> {e.name}</p>
              <p> {e.description}</p>
            </div>
          )
        })} </p>
      </div> */}
      <Router>
        <Routes>
          <Route path="/" element={<NavBar/>}/>
        </Routes>
      </Router>
    </div>
  );
}

export default App;
