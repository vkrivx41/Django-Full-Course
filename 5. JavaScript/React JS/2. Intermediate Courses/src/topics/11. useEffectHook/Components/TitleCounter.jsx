import React, { useEffect, useState } from 'react'

const TitleCounter = () => {
  const [count, setCount] = useState(0)
  const [hasClicked, setHasClicked] = useState(false)

  useEffect(() => {
    if (count < 5){
        console.log("useEffect fired.")
        document.title = "Title: "+ count.toString()
    }
  }, [count])


  return (
    <div>
        <h1>{ count }</h1>
        <button onClick={ () => setCount(prev => prev + 1) }>Increment</button>
        <button onClick={ () => setHasClicked(prev =>  !prev) }>Click</button>
    </div>
  )
}

export default TitleCounter
