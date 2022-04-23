import React from "react";
import { string } from "prop-types";

const ExerciseDetail = (props) => {
    return (
        <>
            <div>
                <div>
                    <div>
                        <h2 className="name-txt">{props.name}</h2>
                        <h3 className="description-txt">Added by: {props.creator}</h3>
                    </div>
                    <div>
                        <p>{props.description}</p>
                    </div>
                </div>
            </div>
        </>


        // <div>
        //     <h1>(Exercise Name)</h1>
        //     <p>(Exercise Description)</p>
        // </div>
    );
};

ExerciseDetail.propTypes = {
    name: string,
    description: string,
};

export default ExerciseDetail;