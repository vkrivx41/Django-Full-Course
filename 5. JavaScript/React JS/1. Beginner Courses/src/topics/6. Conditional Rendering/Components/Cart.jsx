import React from 'react'

const Cart = () => {
  const items  = ["Wireless Earbuds", "Microphone", "Jumper", "New SSD"]

  return (
    <div>
        <h1>Cart 🛒</h1>
        { items.length > 0 && <h2>You have {items.length} items in your cart.</h2> }

        <h2>Items: </h2>
        <ol>
            { items.map(item => (
                <li key={ Math.random() }>{ item }</li>
            )) }
        </ol>
    </div>
  )
}

export default Cart