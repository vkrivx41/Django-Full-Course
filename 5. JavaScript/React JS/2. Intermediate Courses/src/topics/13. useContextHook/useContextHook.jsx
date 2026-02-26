import React, { createContext } from 'react'
import ComponentC from './Components/ComponentC'
import UserProfile from './Components/UserProfile'

import { UserProvider } from './Contexts/UserContext'
import UserUpdate from './Components/UserUpdate'

export const Data = createContext()
export const MoreData = createContext()


const UseContextHook = () => {
  const name = "Pascal Le Grand"
  const age = 21

  return (
    // <Data.Provider value={ name }>
    //   <MoreData.Provider value={ age }>
    //     <ComponentC />
    //   </MoreData.Provider>
    // </Data.Provider>
    <div>
      <UserProvider>
        <UserProfile />
        <UserUpdate />
      </UserProvider>
    </div>
  )
}

export default UseContextHook
