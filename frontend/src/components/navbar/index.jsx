import { Link, Routes, Route } from "react-router-dom";
import SearchBar from "../searchbar";
import { useEffect } from "react";


const NavBar = () => {

    return (
        <>
            <nav>
                {/* Logo for home page? */}
                <a href="/">Home</a>
                <SearchBar/>
                <a href="/profile">Profile</a>
                <Link to="/workouts">
                    Workouts
                </Link>
                <a href="">Groups</a>
                <a href="">Logout</a>
            </nav>

        </>
    );
};

export default NavBar;