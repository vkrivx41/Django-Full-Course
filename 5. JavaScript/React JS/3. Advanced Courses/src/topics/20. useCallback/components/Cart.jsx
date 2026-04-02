import React, { useCallback, useMemo, useState } from 'react'
import ItemForm from './ItemForm'

const Cart = () => {
  const [delivery, setDelivery] = useState(5)

  const [items, setItems] = useState(() => {
    return [
        {name: "Item 1", price: 15},
        {name: "Item 2", price: 19},
        {name: "Item 3", price: 12},
    ]
  })

  const total = useMemo(() => {
    console.log("Heavy Computation")
    return items.reduce((acc, curr) => acc + curr.price, delivery)
  }, [items, delivery])

  const addItemToCart = useCallback((newItem) => {
    setItems(currentItems => [...currentItems, newItem])
  }, [])

  return (
    <div>
        <h1>Cart Items:</h1>
        <ItemForm addNewItem={ addItemToCart } />

        <ul>
            {items.map(item => (
                <li key={item.name}>{item.name} - ${item.price}</li>
            ))}
        </ul>
        <h3>Delivery: ${delivery}</h3>
        <input
            type="number" min="0" max="10"
            placeholder='Delivery'
            value={ delivery }
            onChange={(e) => setDelivery(parseInt(e.target.value))}
        />
        <h2>Total: ${total}</h2>
    </div>
  )
}

export default Cart