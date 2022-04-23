import NavBar from "../../components/navbar";
import Workout from "../../components/workout";

import * as exerciseService from "../../api/exercise.service"

const WorkoutList = () => {
    console.log(exerciseService.getAll())
    return(
        <>
            <NavBar/>
            <h1>Workout List</h1>
            <Workout/>
        </>
    )
}

export default WorkoutList;