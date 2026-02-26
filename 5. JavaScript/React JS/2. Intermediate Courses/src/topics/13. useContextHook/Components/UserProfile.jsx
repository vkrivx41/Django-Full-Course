import React, {useContext} from 'react'

import { UserContext } from './../Contexts/UserContext'

const UserProfile = () => {
  const { user } = useContext(UserContext)

  return (
    <div>
        <h1>User Profile</h1>
        <h3>Name: {user.name} </h3>
    </div>
  )
}

export default UserProfile
