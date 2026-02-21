import React, { useState } from 'react'
import DecreaseCounter from './DecreaseCounter'
import IncreaseCounter from './IncreaseCounter'

const Counter = () => {
  let [count, setCount] = useState(() => {
    console.log("renders only for the first time, because it's a callback")
    return 0
  })

  return (
    <div>
        <h1>Counter</h1>
        <DecreaseCounter count={ count } setCount={ setCount } />
        <span>{ count }</span>
        <IncreaseCounter count={ count } setCount={ setCount } />
    </div>
  )
}

export default Counter
