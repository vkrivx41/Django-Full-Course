import React from 'react'
import RenderCounter from './Components/RenderCounter'
import DomReference from './Components/DomReference'
import Debounce from './Components/Debounce'
import DoubleSubmission from './Components/DoubleSubmission'

const UseRefHook = () => {
  return (
    <div>
      <RenderCounter />
      <DomReference />
      <Debounce />
      <DoubleSubmission />
    </div>
  )
}

export default UseRefHook
