import React, {createContext, useContext, useEffect, useState} from 'react'

export const MeDataContext = createContext()

export const useMe = () =>{
  return useContext(MeDataContext)
}


const MeContext = ({ children }) => {
  const [me, setMe] = useState({})

  useEffect(() => {
    async function fetchData(){
        try {   
          const response = await fetch("http://localhost:8000/me/",{
            method: "GET",
            headers: {
              "Authorization": "Bearer " + "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzc0Mzc3MjgxLCJpYXQiOjE3NzQzMzQwODEsImp0aSI6IjZlYWFlN2RiMDQ3ZTRiMDNhYjJiNzcwYTUxZGY0YjViIiwidXNlcl9pZCI6IjIifQ.CIVik-KeWNfe937e3ygTirzUBXFSKIztmp9ISg0wb0I"
            }
          })
          const data = await response.json()
          if (response.status == 200){
            console.log(data)
            setMe(data)
          }
        } catch (error) {
          console.error("Error Fetching: ", error)
        }
    }

    fetchData()

  }, [])
  
  return (
    <MeDataContext.Provider value={ me }>
        { children }
    </MeDataContext.Provider>
  )
}

export { MeContext }
