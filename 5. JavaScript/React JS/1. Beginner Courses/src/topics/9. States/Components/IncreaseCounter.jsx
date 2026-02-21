import React from 'react'

const IncreaseCounter = ({ count, setCount }) => {
    const increaseCount = () => {
        setCount(prevCount => prevCount + 1)
        setCount(prevCount => prevCount + 1)
    }

  return (
   <button onClick={ increaseCount }>+</button>
  )
}

export default IncreaseCounter