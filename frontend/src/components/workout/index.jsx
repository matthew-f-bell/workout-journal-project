import React, { useEffect, useState } from "react";

const Workout = (props) => {
    const [exerciseList] = useState([])

    const getExercises = async () => {
        props.exercises.forEach(element => console.log(element))

    }

    //console.log(exerciseList)
    
    useEffect(() => {
        getExercises()
    }, [])

    return (
        <>
            <div className="top-workout-div">
                <div className="workout-container">
                    <div className="workout-info">
                        <h2 className="workout-name-txt">{props.name}</h2>
                        <h3 className="workout-creator-txt">{props.creator}</h3>
                    </div>
                    <h2>Exercises:</h2>
                    {props.exercises.map((exercise) => {

                    })}
                    {/* <div className="workout-description-txt">
                        <p>{props.description}</p>
                    </div> */}
                </div>
            </div>
        </>
    )
}

export default Workout;