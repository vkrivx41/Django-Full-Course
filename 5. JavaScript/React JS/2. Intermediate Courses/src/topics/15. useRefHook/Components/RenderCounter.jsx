import React, { useEffect, useState, useRef } from 'react'

const RenderCounter = () => {
  const [name, setName] = useState('')
  const renderCount = useRef(1)
  const previousName = useRef('')

  useEffect(() => {
    renderCount.current += 1
  })

  useEffect(() => {
    previousName.current = name
  }, [name])

  return (
    <div>
        <input type="text" onChange={(e) => setName(e.target.value)} value={ name } />
        <h1>My name is { name } and it used to be {previousName.current}</h1>
        <h3>I rendered { renderCount.current } times</h3>
    </div>
  )
}

export default RenderCounter
