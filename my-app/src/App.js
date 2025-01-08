

import React from 'react';
import { BrowserRouter as Router, Routes, Route, Link } from 'react-router-dom';
import Header from './components/Header';
import Footer from './components/Footer';
import Sidebar from './components/Sidebar';
import Home from './pages/Home';
import About from './pages/About';
import Chat from './pages/Chat';
import './App.css';


function App() {
    return (
        <Router>
            <div className="app-container">
                <div className="main-layout">
                    <Sidebar />
                    <main className="content">
                        <Routes>
                            <Route path="/" element={<Home />} />
                            
                            <Route path="/about" element={<About />} />
                            <Route path="/chat" element={<Chat />} />
                        </Routes>
                    </main>
                </div>
                <Footer />
            </div>
        </Router>
    );
}
export default App;
