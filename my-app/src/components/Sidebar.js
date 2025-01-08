import {Link, useLocation} from 'react-router-dom'
import React from 'react';
import './Sidebar.css'
import logo from '../assets/AI.png';

function Sidebar(){

	const location = useLocation();

	return (
		<div className = 'sidebar'>
		<img src = {logo} alt = "Logo" className ="logo"/>
			<nav>
				<ul>

					<li><Link to ="/" className={location.pathname === '/' ? 'active' : ''}>Home</Link></li>
					<li><Link to ="/chat" className={location.pathname === '/chat'? 'active' : ''}>Chat</Link></li>
					<li><Link to ="/about" className={location.pathname === '/about' ? 'active' : ''}>About</Link></li>
				</ul>
			</nav>
		</div>
	);
}

export default Sidebar;