import React, { useState } from 'react';
import * as AuthService from "../../api/auth.service";

const SignUp = () => {
    const [email, setEmail] = useState("");
    const [password, setPassword] = useState("");

    const handleSubmit = async (e) => {
        e.preventDefault();
        await AuthService.register(email, password).then(() => {
            setEmail = "";
            setPassword = "";
        });
    };


    return (
        <div>
            <div>
                <h2>Sign-Up Page</h2>
                <form method="post">
                    <label for="email">
                        email
                    </label>
                    <input
                        type="email"
                        name="email"
                        onChange={(e) => setEmail(e.target.value)}
                        value={email}
                        placeholder="email"
                    />
                    <label for="password1">
                        password
                    </label>
                    <input
                        type="password"
                        name="password1"
                        onChange={(e) => setPassword(e.target.value)}
                        value={password}
                        placeholder="password"
                    />
                    <input type="submit" value="Sign-Up" onClick={handleSubmit} />
                </form>
            </div>
        </div>
    )
}

export default SignUp;