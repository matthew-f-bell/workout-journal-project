const CreateWorkout = () => {
    return (
        <>
            <h2>Create Workout</h2>
            <form action="post">
                <label for="name">Name</label>
                <input type="text" name="name"/>

                <label for="reps">Number of Reps</label>
                <input type="text" name="reps"/>

                <label for="sets">Number of Sets</label>
                <input type="text" name="sets"/>

                <input type="submit" value="Create"/>
                <button>Cancel</button>
            </form>
        </>
    )
}

export default CreateWorkout;