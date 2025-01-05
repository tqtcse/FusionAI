import React from 'react';
import { Link } from 'react-router-dom';
import logo from '../assets/AI.png'; // Đường dẫn đến tệp logo
import './Header.css'; // Tệp CSS cho Header

function Header() {
    return (
        <header className="header">
            <div className="header-content">
                <h1 className="site-title">AI Fusion</h1>
                <img src={logo} alt="Logo" className="logo" />
            </div>
            <nav>
                <Link to="/">Home</Link> {' | '}
                <Link to="/about">About</Link>
                <Link to="/chat">Chat</Link>
            </nav>
        </header>
    );
}

export default Header;
