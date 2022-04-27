import React, { useState } from 'react';
import * as AuthService from "../../api/auth.service"

const Login = () => {
    const [email, setEmail] = useState("");
    const [password, setPassword] = useState("");

    const handleSubmit = async (e) => {
        e.preventDefault();
        await AuthService.login(email, password).then(() => {
            setEmail = "";
            setPassword = "";
        });
    };
    return (
        <>
            <h2>Login</h2>
            <form action="post">
                <label for="email">E-mail</label>
                <input
                    type="text"
                    name="email"
                    onChange={(e) => setEmail(e.target.value)}
                    value={email}
                    placeholder="email"
                />

                <label for="password">Password</label>
                <input
                    type="password"
                    name="password"
                    onChange={(e) => setPassword(e.target.value)}
                    value={password}
                    placeholder="password"
                />

                <input type="submit" value="Login" onClick={handleSubmit}/>
            </form>
        </>
    )
}

export default Login;