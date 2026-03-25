import React, { useMemo, useState } from 'react'

const slowFunction = (num) => {
  for (let i = 0; i < 100_000_000; i++) { }
  return num * 2
}


const ThemeNumberSimulation = () => {
  const [number, setNumber] = useState(0)
  const [dark, setDark] = useState(false)

  const result = useMemo(() => {
    return slowFunction(number)
  }, [number])

  const styles = {
    backgroundColor: dark ? "black" : "gray",
    color: dark ? "white" : "black",
    padding: "10px"
  }

  return (
    <div>
      <input type="number" value={number} onChange={(e) => setNumber(parseInt(e.target.value))} />
      <button onClick={() => setDark(theme => !theme)}>Toggle Theme</button>
      <div style={styles}>{result}</div>
    </div>
  )
}

export default ThemeNumberSimulation