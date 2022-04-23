import React from "react";
import { string } from "prop-types";

const WorkoutList = (props) => {
    return (
        // <div>
        //     <h1>Workouts</h1>
        //     <span><a href="">(Workout Names)</a></span>
        // </div>
        <>
            <div className="top-workout-div">
                <div className="workout-container">
                    <div className="workout-info">
                        <h2 className="workout-name-txt">{props.name}</h2>
                        <h3 className="workout-creator-txt">{props.creator}</h3>
                    </div>
                    <div className="workout-description-txt">
                        <p>{props.description}</p>
                    </div>
                </div>
            </div>
        </>
    )
}

export default WorkoutList;