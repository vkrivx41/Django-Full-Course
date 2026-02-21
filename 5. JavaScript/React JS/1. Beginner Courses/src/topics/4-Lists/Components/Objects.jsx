import React from 'react'

const Objects = () => {
  let userInfo = [
    {
        "username": "Nik",
        "email": "nik@gmail.com",
        "location": "Gisozi",
    },
    {
        "username": "Bun",
        "email": "bun@gmail.com",
        "location": "Remera",
    },
    {
        "username": "Teta",
        "email": "teta@yahoo.com",
        "location": "Gisozi",
    },
    {
        "username": "Keza",
        "email": "keza@mineduc.gov.rw",
        "location": "Kinyinya",
    },
  ]

  return (
    <div>
        { userInfo.map(({ username, email, location }) => (
            <ul>
                <li>{ username }</li>
                <li>{ email }</li>
                <li>{ location }</li>
            </ul>
        ))  }
    </div>
  )
}

export default Objects
