import React, { useState, lazy, Suspense, useTransition } from 'react'
// import { AdminData } from '../components/AdminData'

import lazyLoad from './../utilities/lazyLoad.js'

const AdminData = lazyLoad("./../Components/AdminData", "AdminData")

const Home = () => {
  const [isAdmin, setIsAdmin] = useState(false)
  const [isPending, startTransition] = useTransition()

  return (
    <>
      <h1>Home</h1>
      <button onClick={() => {
        import("../utilities/add.js").then(module => {
          return alert(module.add(2, 2))
        })
      }}>Add 2 + 2</button>
      <br />
      <br />
      <button onClick={() => {
        startTransition(() => {
          setIsAdmin(current => !current)
        })
      }}
      >Toggle Admin</button>
      {isPending && "Loading..."}
      <Suspense fallback={<h2>Loading...</h2>}>
        {isAdmin ? <AdminData /> : <h2>Not Admin</h2>}
      </Suspense>
    </>
  )
}

export default Home
