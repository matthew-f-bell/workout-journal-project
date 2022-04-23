import { useEffect, useReducer } from "react";

import NavBar from "../../components/navbar";
import WorkoutList from "../../components/workoutlist";


const HomePage = () => {

    return (
        <>
            <NavBar />
            <h1>Home Page</h1>
            <WorkoutList />
        </>
    )
}

export default HomePage;