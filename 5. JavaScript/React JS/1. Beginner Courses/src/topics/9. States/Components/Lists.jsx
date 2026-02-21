import React, { useState } from 'react'

const Lists = () => {
  const [cars, setCars] = useState(() => ["Lambo", "BMW"])
  const [carName, setCarName] = useState("")
  
  const handleSubmit = (e) => {
    e.preventDefault()

    if (carName){
        setCars(prevCars => {
            return [...prevCars, carName]
        })
    }
    setCarName(() => "")

  }

  const handleCarDelete = (e) => {
    const selectedCar = e.target.innerText

    setCars(prevCars => {
        return prevCars.filter(car => car !== selectedCar)
    })
  }

  const handleInput = (e) => {
    setCarName(() => e.target.value )
  }

  return (
    <div>
        <h1>Cars</h1>
        <form onSubmit={ handleSubmit }>
            <input type="text" value={ carName } onInput={ handleInput } />
            <button type="submit">Add</button>
        </form>
        <ul>
            { cars.map(car => (
                <li key={ Math.random() } onClick={ handleCarDelete }>{ car }</li>
            )) }
        </ul>
    </div>
  )
}

export default Lists