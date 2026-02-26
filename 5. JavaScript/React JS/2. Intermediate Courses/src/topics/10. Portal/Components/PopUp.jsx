import React from 'react'
import { createPortal } from 'react-dom'


const PopUp = ({ copied }) => {
  
  const styles = {
    position: "absolute",
    bottom: "30px",
    transition: "bottom 2s ease"
  }

  return createPortal(
    <div style={ styles }>
        {copied && <span>Copied to clipboard</span> }
    </div>,
    document.getElementById("pop-up-content")
  )
}

export default PopUp
