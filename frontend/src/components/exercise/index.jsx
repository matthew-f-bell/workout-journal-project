import { useEffect, useState } from "react"
import * as exerciseService from "../../api/exercise.service"

const Exercise = (props) => {
    const [exerciseName, setExerciseName] = useState("")

    const getExercise = async () => {
        await exerciseService.get(props.exerciseID).then((res) => {
            setExerciseName(res.data.name)
        })
    }

    useEffect(() => {
        getExercise()
    }, [])

    return (
        <>
            <h3>{exerciseName}</h3>
            <p>Number of Sets: {props.sets}</p>
            <p>Number of Reps: {props.reps}</p>
        </>
    )
}

export default Exercise