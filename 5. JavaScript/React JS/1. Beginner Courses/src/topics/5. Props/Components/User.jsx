import React from 'react'

const User = (props) => {
  return (
    <>
        <h1>{ props.name }</h1>
        <h2>{ props.age }</h2>
        <h3>{ props.hobbies }</h3>
        <h4>{ props.isMarried ? "Married": "Not Married" }</h4>
    </>
  )
}

export default User
