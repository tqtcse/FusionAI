import React from 'react';
import { Link } from 'react-router-dom';

function Header() {
    return (
        <header className="header">
            <h1>Fusion AI</h1>
            <nav>
                <Link to="/">Home</Link> 
                {' | '}
                <Link to="/about">About</Link>
            </nav>
        </header>
    );
}

export default Header;
