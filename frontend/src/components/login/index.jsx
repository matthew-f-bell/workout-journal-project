import React from 'react';


const Login = () => {
    return (
        <>
            <h2>Login</h2>
            <form action="post">
                <label for="email">E-mail</label>
                <input type="text" name="email"/>

                <label for="password">Password</label>
                <input type="text" name="password"/>

                <input type="submit" value="Login"/>
            </form>
        </>
    )
}

export default Login;