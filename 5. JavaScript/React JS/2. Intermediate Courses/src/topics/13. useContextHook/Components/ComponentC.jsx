import React, { useContext } from 'react'

import { Data, MoreData } from './../useContextHook'

const ComponentC = () => {

  const name = useContext(Data)
  const age = useContext(MoreData)

  return (
    <h1>My name is { name }, I'm { age }.</h1>
  )
}

export default ComponentC
