import React from 'react';
import ProductList from '../components/ProductList';

function Home() {
    const products = [
        { id: 1, name: 'Product 1', price: 50 },
        { id: 2, name: 'Product 2', price: 30 },
        { id: 3, name: 'Product 3', price: 20 },
    ];

    return (
        <div className="home-page">
            <h2>Welcome to the Home Page</h2>
            <ProductList products={products} />
        </div>
    );
}

export default Home;
