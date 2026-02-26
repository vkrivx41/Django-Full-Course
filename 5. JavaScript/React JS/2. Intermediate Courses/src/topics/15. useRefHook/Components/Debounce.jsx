import { useState, useRef } from 'react'


const Debounce = () => {
  const [name, setName] = useState("")
  const timeoutRef = useRef(null)

  const handleChange = (e) => {
    const value = e.target.value
    setName(value)

    if (timeoutRef.current){
        clearTimeout(timeoutRef.current)
    }
    
    timeoutRef.current = setTimeout(() => {
        console.log(value)
        console.log("Waited 1 sec to write")
    }, 1000);
  }

  return (
    <div>
        <h1>Debounce</h1>
        <input type="text" value={ name } onChange={ handleChange } />
        <h2>My name is { name }</h2>
    </div>
  )
}

export default Debounce