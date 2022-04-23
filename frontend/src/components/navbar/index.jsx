import { Link, Routes, Route } from "react-router-dom";
import SearchBar from "../searchbar";
import { useEffect } from "react";


const NavBar = ({ fetchAllExercises, exercises }) => {

    const handleExercises = async() => {
        await fetchAllExercises();
    }
    return (
        <>
            <nav>
                {/* Logo for home page? */}
                <a href="/">Home</a>
                <SearchBar/>
                <a href="">Profile</a>
                <Link to="/workouts" onClick={handleExercises}>
                    Workouts
                </Link>
                <a href="">Groups</a>
                <a href="">Logout</a>
            </nav>

        </>
    );
};

export default NavBar;