// // import logo from './logo.svg';
// import React, {useEffect, useState} from 'react';
// import './App.css';
// import fetchData from './API/api';
// import ProductList from './component/ProductList';

// // function App() {
// //   return (
// //     <div className="App">

// //       // <header className="App-header">
// //       //   <img src={logo} className="App-logo" alt="logo" />
// //       //   <p>
// //       //     Edit <code>src/App.js</code> and save to reload.
// //       //   </p>
// //       //   <a
// //       //     className="App-link"
// //       //     href="https://reactjs.org"
// //       //     target="_blank"
// //       //     rel="noopener noreferrer"
// //       //   >
// //       //     Learn React
// //       //   </a>
// //       // </header>
// //     </div>
// //   );
// // }

// // export default App;



// function App() {
//   const products = [
//         { id: 1, name: 'Product 1', price: 50 },
//         { id: 2, name: 'Product 2', price: 30 },
//     ];
//   const [data, setData] = useState(null);  // Trạng thái để lưu trữ dữ liệu API
//   const [error, setError] = useState(null); // Trạng thái để lưu trữ lỗi

//   useEffect(() => {
//   fetchData()
//       .then((data) => {
//         setData(data); // Cập nhật dữ liệu vào state
//       })
//       .catch((err) => {
//         setError('Failed to fetch data'); // Cập nhật lỗi nếu có
//       });


// }, []);

//   return (
//     <div className="App">
//        <h1>Welcome to React Shop</h1>
//             <ProductList products={products} />

//       {error && <p>{error}</p>} {/* Hiển thị lỗi nếu có */}
//       {data ? (
//         <pre>{JSON.stringify(data, null, 2)}</pre>  // Hiển thị dữ liệu API
//       ) : (
//         <p>Loading...</p>
//       )}
//     </div>
//   );
// }

// export default App;

import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Header from './components/Header';
import Footer from './components/Footer';
import Home from './pages/Home';
import About from './pages/About';
import './App.css';

function App() {
    return (
        <Router>
            <div className="App">
                <Header />
                <main className="content">
                    <Routes>
                        <Route path="/" element={<Home />} />
                        <Route path="/about" element={<About />} />
                    </Routes>
                </main>
                <Footer />
            </div>
        </Router>
    );
}

export default App;
