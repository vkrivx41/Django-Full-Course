import React from 'react'

const Card2 = () => {

  const divStyles = {
    color: "lightblue",
    backgroundColor: "darkblue",
    padding: "10px",
    borderRadius: "4px",
  }

  const titleStyles = {
    fontSize: "30px"
  }

  return (
    <div style={ divStyles } className='card'>
        <div className="title" style={ titleStyles }>Content Title</div>
        <div className="body">Content body goes here</div>
    </div>
  )
}

export default Card2
