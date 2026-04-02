import React, { Suspense } from 'react'
import { NavLink, Outlet } from 'react-router-dom'

const NavWrapper = () => {
  return (
    <>
      <nav style={{ display: "flex", gap: "6px" }}>
        <NavLink to='/'>Home</NavLink>
        <NavLink to='/store'>Store</NavLink>
        <NavLink to='/about'>About</NavLink>
      </nav>
      <Suspense fallback={<h1>Loading...</h1>}>
        <Outlet />
      </Suspense>
    </>
  )
}

export default NavWrapper
