import { useState, useRef } from 'react'


const DomReference = () => {

  const [name, setName] = useState('')
  const nameInput = useRef()

  const setFocus = () => {
    nameInput.current.focus()
  }

  return (
    <div>
        <hr />
        <button onClick={ setFocus }>Focous</button>
        <input type="text" value={ name } onInput={(e) => setName(e.target.value)} ref={ nameInput }/>
        <h1>My name is { name }</h1>
    </div>
  )
}

export default DomReference