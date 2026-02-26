import React, { createContext } from 'react'
import ComponentA from './Components/ComponentA'
import ComponentC from './Components/ComponentC'


export const Data = createContext()
export const MoreData = createContext()


const ContextAPI = () => {
  const name = "Scorpus"
  const age = 21

  return (
    <Data.Provider value={ name }>
      <MoreData.Provider value={ age }>
        <ComponentC />
      </MoreData.Provider>
    </Data.Provider>
  )
}

export default ContextAPI
