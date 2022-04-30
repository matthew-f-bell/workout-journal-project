import NavBar from "../../components/navbar";
import Profile from "../../components/profile";
import Login from "../../components/login";
import SignUp from "../../components/signup";
import { NavLink } from "react-router-dom";

const HomePage = () => {

    return (
        <>
            <NavBar />
            <h1>Home Page</h1>
            <Login />
            <NavLink to="/register">Sign-Up</NavLink>
        </>
    )
}

export default HomePage;