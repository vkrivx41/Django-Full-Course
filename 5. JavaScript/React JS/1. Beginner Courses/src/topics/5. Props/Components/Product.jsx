import React from 'react'

const Product = ({ name, price }) => {
  return (
    <div>
        <h1>{ name }</h1>
        <h2>${ price.toLocaleString() }</h2>
    </div>
  )
}

export default Product
