import React from 'react'
import { MdOutlineSubtitles } from "react-icons/md";
import { IoDocumentText } from "react-icons/io5";


import './../css/index.css'


const Card3 = () => {
  return (
    <div className="card">
        <div className="title"><MdOutlineSubtitles /> Content Title</div>
        <div className="body"><IoDocumentText /> Content body goes here</div>
    </div>
  )
}

export default Card3
