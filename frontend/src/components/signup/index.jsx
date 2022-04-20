const SignUp = () => {
    return (
        <div>
            <div>
                <h2>Sign-Up Page</h2>
                <form action="post">
                    <label for="email">
                        email
                    </label>
                    <input type="email" name="email" />
                    <label for="password1">
                        password
                    </label>
                    <input type="password" name="password1" />
                    <label for="password2">
                        confirm password
                    </label>
                    <input type="password" name="password2" />
                    <input type="submit" value="Sign-Up" />
                </form>
            </div>
        </div>
    )
}

export default SignUp;