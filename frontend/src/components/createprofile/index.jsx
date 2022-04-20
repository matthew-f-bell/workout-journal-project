const CreateProfile = () => {
    return (
        <div>
            <div>
                <h2>Create Your Profile</h2>
                <form method="post">
                    <label for="first-name">
                        First Name:
                    </label>
                    <input type="text" name="first-name" required />
                    <label for="last-name">
                        Last Name:
                    </label>
                    <input type="text" name="first-name" required />
                    <label for="user-height">
                        Height:
                    </label>
                    <input type="number" name="user-height" required />
                    <label for="user-weight">
                        Weight: 
                    </label>
                    <input type="number" name="user-weight" required />
                    <label for="profile-pic">
                        Profile Picture:
                    </label>
                    <input type="file" name="profile-pic" accept="image/" />
                    <input type="submit" value="Save" />
                </form>
            </div>
        </div>
    )
}

export default CreateProfile;