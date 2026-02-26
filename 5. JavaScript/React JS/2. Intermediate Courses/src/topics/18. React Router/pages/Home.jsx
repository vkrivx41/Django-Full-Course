import React, { useEffect, useRef, useState } from 'react'
import { useSearchParams } from 'react-router-dom'

const Home = () => {
  const [searchParams, setSearchParams] = useSearchParams({name: ""})
  const postName = searchParams.get("name")

  const fetchTimeout = useRef(null)

  useEffect(() => {
    if (fetchTimeout.current){
        clearTimeout(fetchTimeout.current)
    }

    fetchTimeout.current = setTimeout(() => {
        if (postName != "" && postName != null){
            console.log("fetching data after 2 secs of no typing and not empty post name")
        }
    }, 2000);

  }, [postName])


  return (
    <>
        <h1>Home</h1>
        <h2>Search Post: { postName }</h2>
        <input type="text" value={ postName } onChange={(e) => setSearchParams({name: e.target.value})} />
    </>
  )
}

export default Home