import React from 'react'

const Card1 = () => {
  return (
    <div style={
        { color: "lightblue", backgroundColor: "darkblue", borderRadius: "4px", padding: "10px" }
    } className='card'>
        <div className="title" style={{ fontSize:"30px" }}>Content Title</div>
        <div className="body">Content body goes here</div>
    </div>
  )
}

export default Card1
