import React from 'react'
import Password from './Components/Password'
import Cart from './Components/Cart'
import Weather from './Components/Weather'
import UserStatus from './Components/UserStatus'


const Conditional = () => {
  return (
    <div>
        <Password isValid={ true } />
        <Cart />
        <Weather temperature={ 34 } />
        <UserStatus isLoggedIn={ true } isAdmin={ false } />
    </div>
  )
}

export default Conditional
