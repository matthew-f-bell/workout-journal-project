import { NavLink } from "react-router-dom";
import NavBar from "../../components/navbar";
import SignUp from "../../components/signup";

const SignupPage = () => {

    return (
        <>
            <NavBar />
            <h1>Sign-Up</h1>
            <SignUp />
            <NavLink to="/">Login</NavLink>
        </>
    )
}

export default SignupPage;