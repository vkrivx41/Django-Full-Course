import React from 'react'
import { NavLink } from 'react-router-dom'

import './../css/style.css'

const NavBar = () => {
  return (
    <ul>
      <li>
        <NavLink to="/" active>Home</NavLink>
      </li>
      <li>
        <NavLink to="/posts" end>Posts</NavLink>
      </li>
    </ul>
  )
}

export default NavBar
