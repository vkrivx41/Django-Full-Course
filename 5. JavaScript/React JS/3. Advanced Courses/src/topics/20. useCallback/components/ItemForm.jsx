import React, { useState } from 'react'


const ItemForm = ({ addNewItem }) => {
  console.log("Child")
  const [itemName, setItemName] = useState('')
  const [itemPrice, setItemPrice] = useState(0)

  const addItem = () => {
    addNewItem({name: itemName, price: itemPrice})

    setItemName('')
    setItemPrice(0)
  }
  
  return (
    <>
        <input
            type="text"
            placeholder='Item Name'
            value={ itemName }
            onChange={(e) => setItemName(e.target.value)}
        />
        <input
            type="number" min="0" max="99"
            placeholder='Price'
            value={ itemPrice }
            onChange={(e) => setItemPrice(parseInt(e.target.value))}
        />
        <button onClick={() => addItem() }>Add Item</button>
    </>
  )
}

export default React.memo(ItemForm)