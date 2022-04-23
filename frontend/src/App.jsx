import { BrowserRouter, Routes, Route } from 'react-router-dom'
import HomePage from "./pages/homepage"
import ProfilePage from './pages/profilepage';
import WorkoutList from './pages/workoutlist';


function App() {

  return (
    <div className="App">
      <BrowserRouter>
        <Routes>
          <Route path="/" element={<HomePage/>}/>
          <Route path="/workouts" element={<WorkoutList/>}/>
          <Route path="/profile" element={<ProfilePage/>}/>
        </Routes>
      </BrowserRouter>
    </div>
  );
}

export default App;