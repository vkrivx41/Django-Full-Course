import React, { useEffect } from 'react'
import { Navigate, useNavigate } from 'react-router-dom'

const NotFound = () => {
  const navigate = useNavigate()

  useEffect(() => {
    const redirectTimeout = setTimeout(() => {
      navigate("/", {})
      // navigate(-1, {})  // prev page
    }, 1000)

    return (() => {
      clearTimeout(redirectTimeout)
    })
  }, [])

  return (
    <>
      <h1>Not Found</h1>
    </>
  )
}

export default NotFound