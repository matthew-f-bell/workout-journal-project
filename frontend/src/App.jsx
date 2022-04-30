import { BrowserRouter, Routes, Route } from 'react-router-dom'
import HomePage from "./pages/homepage"
import ProfilePage from './pages/profilepage';
import SignupPage from './pages/signuppage';
import WorkoutList from './pages/workoutlist';


function App() {

  return (
    <div className="App">
      <BrowserRouter>
        <Routes>
          <Route path="/" element={<HomePage/>}/>
          <Route path="/workouts" element={<WorkoutList/>}/>
          <Route path="/profile" element={<ProfilePage/>}/>
          <Route path="/register" element={<SignupPage/>}/>
        </Routes>
      </BrowserRouter>
    </div>
  );
}

export default App;