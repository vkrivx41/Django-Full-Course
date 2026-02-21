import React from 'react'

const Button = () => {

  const handleClick = (e) => {
    console.log("You Clicked Me")
    console.log(Math.floor(Math.random() * 100))
  }

  const handleCopy = (e) => {
    alert("Stop Copying My Content")
  }

  const handleMove = (e) => {
    alert("You've moved across the text")
  }

  const styles = {
    padding: "20px",
    fontSize: "30px",
  }

  return (
    <div>
        <button onClick={ handleClick } style={ styles }>Click</button>
        <p onCopy={ handleCopy } onMouseOver={ handleMove }>
            Lorem ipsum dolor sit amet consectetur adipisicing elit. Veniam explicabo voluptatum repellendus dicta provident unde quis, quaerat sapiente beatae nobis commodi aliquid magnam dignissimos. Suscipit saepe commodi corporis eveniet sed.
        </p>
    </div>
  )
}

export default Button