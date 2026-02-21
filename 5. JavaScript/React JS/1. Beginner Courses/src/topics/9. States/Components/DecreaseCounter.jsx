import React from 'react'

const DecreaseCounter = ({ cout, setCount }) => {
    const decreaseCount = () => {
        setCount(prevCount => {
            return prevCount - 1
        })
    }

  return (
    <button onClick={ decreaseCount }>-</button>
  )
}

export default DecreaseCounter
