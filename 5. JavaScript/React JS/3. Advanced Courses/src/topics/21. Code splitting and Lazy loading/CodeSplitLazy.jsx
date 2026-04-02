import React, { lazy } from 'react'
import { BrowserRouter, Routes, Route } from 'react-router-dom'
import NavWrapper from './components/NavWrapper'
import lazyLoad from './utilities/lazyLoad'
// import Home from './pages/Home'
// import Store from './pages/Store'
// import { About } from './pages/About'

const Home = lazyLoad("./../pages/Home")
const Store = lazyLoad("./../pages/Store")
const About = lazyLoad("./../pages/About", "About")

const CodeSplitLazy = () => {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<NavWrapper />}>
          <Route path='/' element={<Home />} />
          <Route path='/store' element={<Store />} />
          <Route path='/about' element={<About />} />
        </Route>
      </Routes>
    </BrowserRouter>
  )
}

export default CodeSplitLazy
