import React, { useCallback, useMemo, useState } from 'react'
import Child from './Child'


const ChildRenderSimulation = () => {
  const [localNumber, setLocalNumber] = useState(0)
  const [childNumber, setChildNumber] = useState(0)

  const [arr, setArr] = useState([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
  const memoizedLargest = useMemo(() => getLargestNumber(), [arr])

  const setChildNum = useCallback((newNum) => {
    setChildNumber(newNum)
  }, [])

  function getLargestNumber(){
    console.log("Heavy Computation")
    return Math.max(...arr)
  }

  const changeArray = () => {
    setArr([30, 40, 50, 60])
  }

  return (
    <div>
        <h1>Local: {localNumber}</h1>
        <button onClick={() => setLocalNumber(state => state + 1)}>Change Local</button>
        <Child number={childNumber} changeNumber={setChildNum} />
        <h1>Largest: { memoizedLargest }</h1>
        <button onClick={() => changeArray()}>Change Array</button>
    </div>
  )
}

export default ChildRenderSimulation
