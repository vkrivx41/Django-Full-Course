import React from 'react'

const Child = (props) => {
  console.log("Child")

  const changeChildNumber = () => {
    return props.changeNumber(Math.random())
  }

  return (
    <div>
        <h1>Child: {props.number} </h1>
        <button onClick={changeChildNumber}>Change Child</button>
    </div>
  )
}

export default React.memo(Child)
