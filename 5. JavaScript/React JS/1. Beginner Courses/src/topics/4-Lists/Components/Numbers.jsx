import React from 'react'

const Numbers = () => {
  let numbersList = [1, 2, 3, 4, 5]

  return (
    <div>
      <ul>
        { numbersList.map(number => (
          <li key={number}>{ number }</li>
        ))  }
      </ul>
    </div>
  )
}

export default Numbers
