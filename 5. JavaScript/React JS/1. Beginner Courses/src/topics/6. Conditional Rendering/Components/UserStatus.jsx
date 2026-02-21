import React from 'react'

const UserStatus = ({ isLoggedIn, isAdmin }) => {
    // if (isLoggedIn){
    //     if (isAdmin){
    //         return <h1>Welcome Admin</h1>
    //     }
    //     return <h1>Welcome User</h1>
    // }

    return  isLoggedIn && isAdmin && <h1>Welcome Admin</h1> || isLoggedIn && <h1>Welcome User</h1>
}

export default UserStatus
