import React, { useState } from 'react'
import PopUp from './Components/PopUp'

const Portal = () => {
  const [inputValue, setInputValue] = useState("")
  const [copied, setCopied] = useState(false)
  
  const handleCopy = (e) => {
    e.preventDefault()

    navigator.clipboard.writeText(inputValue).then(() => {
        setCopied(true)
        setTimeout(() => setCopied(false), 3000)
    })
  }

  return (
    <div>
        <h1>Copy the Text</h1>
        <input type="text" onChange={ (e => setInputValue(e.target.value)) } />
        <button onClick={ handleCopy }>Copy</button>

        <PopUp copied={ copied } ></PopUp>
    </div>
  )
}

export default Portal
