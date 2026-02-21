import React from 'react'

const ProductInfo = () => {
  let product = {
    "name": "Laptop",
    "price": 1200,
    "availability": "In Stock",
  }

  return (
    <div>
      <p>Name: { product.name }</p>
      <p>Price: ${ product.price }</p>
      <p>Availability: { product.availability }</p>
    </div>
  )
}

export default ProductInfo