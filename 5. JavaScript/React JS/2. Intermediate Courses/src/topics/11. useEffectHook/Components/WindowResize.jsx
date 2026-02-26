import React, { useEffect, useState } from 'react'

const WindowResize = () => {
  const [windowWidth, setWindowWidth] = useState(window.innerWidth)

  const handleResize = () => {
    setWindowWidth(window.innerWidth)
  }

  useEffect(() => {
    window.addEventListener('resize', handleResize)

    return () => {
        window.removeEventListener('resize', handleResize)
    }

  }, [])

  return (
    <h1>
        { windowWidth }
    </h1>
  )
}

export default WindowResize
