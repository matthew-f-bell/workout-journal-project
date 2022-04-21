import { useState, useEffect } from "react"
import { BrowserRouter, Routes, Route } from 'react-router-dom'
import axios from "axios"
import HomePage from "./pages/homepage"


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
      <BrowserRouter>
        <Routes>
          <Route path="/" element={<HomePage/>}/>
        </Routes>
      </BrowserRouter>
    </div>
  );
}

export default App;
