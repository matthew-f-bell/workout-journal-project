import tellWorkoutTo from "./axios.config";

const exercises = "/exercises";



const getAll = () => {
    return tellWorkoutTo.get(`${exercises}`);
};

const get = (id) => {
    return tellWorkoutTo.get(`${exercises}/${id}`);
};

const create = (data) => {
    return tellWorkoutTo.post(`${exercises}`, data);
};

const update = (id, data) => {
    return tellWorkoutTo.put(`${exercises}/${id}`, data);
};

const destroy = (id) => {
    return tellWorkoutTo.delete(`${exercises}/${id}`);
};



export { getAll, get, create, update, destroy };