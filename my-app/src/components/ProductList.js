import React from 'react';

function ProductList({ products }) {
    return (
        <div className="product-list">
            <h2>Product List</h2>
            <ul>
                {products.map((product) => (
                    <li key={product.id} className="product-item">
                        <h3>{product.name}</h3>
                        <p>Price: ${product.price}</p>
                    </li>
                ))}
            </ul>
        </div>
    );
}

export default ProductList;
