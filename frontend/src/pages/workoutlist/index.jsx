import NavBar from "../../components/navbar";
import Workout from "../../components/workout";

import * as workoutService from "../../api/workout.service"
import { useEffect, useState } from "react";

const WorkoutList = () => {
    const [workouts, setWorkouts] = useState([])

    const getWorkouts = async () => {
        await workoutService.getAll().then((res) => {
            setWorkouts(res.data)
        })
    }

    useEffect(() => {
        getWorkouts()
    }, [])

    return(
        <>
            <NavBar/>
            <h1>Workout List</h1>
            {workouts.map((workout) => {
                return (
                    <>
                        <Workout name={workout.name} creator={workout.creator} exercises={workout.exercises}/>
                    </>
                )
            })}
        </>
    )
}

export default WorkoutList;