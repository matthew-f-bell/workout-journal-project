import React, { useEffect, useState } from "react";
import Exercise from "../exercise"

const Workout = (props) => {
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
                        return (
                            <>
                                <Exercise exerciseID={exercise.exercise} sets={exercise.sets} reps={exercise.reps} />
                            </>
                        )
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