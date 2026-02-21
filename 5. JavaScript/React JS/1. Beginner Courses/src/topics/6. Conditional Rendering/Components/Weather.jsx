import React from 'react'


const Weather = ({ temperature }) => {
  if (temperature < 15){
    return <h1>It's cold 🥶 outside</h1>
  } else if (temperature > 24) {
    return <h1>It's hot 🔥 outside</h1>
  }

  return <h1>It's fine outside</h1>
}

export default Weather
