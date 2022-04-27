import NavBar from "../../components/navbar";
import Profile from "../../components/profile";
import Login from "../../components/login";
import SignUp from "../../components/signup";

const HomePage = () => {

    return (
        <>
            <NavBar />
            <h1>Home Page</h1>
            <Login />
            <SignUp />
        </>
    )
}

export default HomePage;