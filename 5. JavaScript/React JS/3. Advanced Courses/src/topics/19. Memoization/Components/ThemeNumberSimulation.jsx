import React, { useEffect, useMemo, useState } from 'react'

const slowFunction = (num) => {
  console.log("Slow Function")
  for (let i = 0; i < 200_000_000; i++) { }
  return num * 2
}


const ThemeNumberSimulation = () => {
  const [number, setNumber] = useState(0)
  const [dark, setDark] = useState(false)

  const result = useMemo(() => {
    return slowFunction(number)
  }, [number])

  console.log(result)
  
  const styles = useMemo(() => {
    return {
      backgroundColor: dark ? "black" : "gray",
      color: dark ? "white" : "black",
      padding: "10px"
    }
  }, [dark])
  
  useEffect(() => {
    themeChanged()  
  }, [styles])

  const themeChanged = () => {
    console.log("theme changed")
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
