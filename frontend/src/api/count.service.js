import tellWorkoutTo from "./axios.config";

const exercises = "/counts";

const get = (id) => {
    return tellWorkoutTo.get(`${exercises}/${id}/`);
};

export { get };