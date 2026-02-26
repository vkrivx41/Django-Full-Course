import React, { useContext, useState } from 'react'
import { UserContext } from '../Contexts/UserContext'

const UserUpdate = () => {
  const [newName, setNewName] = useState("")
  const { updateUser } = useContext(UserContext)

  const handleSubmit = (e) => {
    e.preventDefault()
    if (newName !== null && newName !== ""){
        updateUser(newName.trim())
        setNewName("")
    }
  }

  return (
    <div>
        <h3>Update User Name</h3>
        <form onSubmit={ handleSubmit }>
            <input
                type="text"
                onChange={(e) => setNewName(e.target.value)}
                value={ newName }
                placeholder="Enter new name"
            />
            <button type="submit" >Update</button>
        </form>
    </div>
  )
}

export default UserUpdate