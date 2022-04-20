const CreateExercise = () => {
    return (
        <>
            <h2>Create Workout</h2>
            <form action="post">
                <label for="name">Name</label>
                <input type="text" name="name"/>

                <label for="description">Description</label>
                <input type="text" name="description"/>

                <input type="submit" value="Create"/>
                <button>Cancel</button>
            </form>
        </>
    )
}

export default CreateExercise;