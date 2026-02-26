import React from 'react'
import TitleCounter from './Components/TitleCounter'
import Data from './Components/Data'
import WindowResize from './Components/WindowResize'

const UseEffectHook = () => {
  return (
    <div>
      <TitleCounter />
      <Data />
      <WindowResize />
    </div>
  )
}

export default UseEffectHook
