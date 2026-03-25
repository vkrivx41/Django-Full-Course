import React, {useState, useEffect} from 'react'
import {Link} from 'react-router-dom'

import {useMe} from './../context/MeContext'

const Document = () => {
  const [documents, setDocuments] = useState([])
  const me = useMe()

  const permissions = me.permissions
  console.log(permissions)
  
  useEffect(() => {

    async function fetchData(){
        const response = await fetch("http://localhost:8000/")
        const data = await response.json()
    
        if (response.status == 200){
          console.log(me)
          setDocuments(data)
        }
    }

    fetchData()
    
  }, [me])

  return (
    <div>
      <nav>
        <h1>Documents</h1>
        <div className="links">
          <a href="">Logout</a>
        </div>
      </nav>
      <hr />
      <ul>
        {permissions}
        {/* {me.permissions.includes("app_core.share_document") && <div>hi</div>} */}
        {documents.map(document => (
            <li key={document.id}>
                <a href="">{document.title}</a>
            </li>
        ))}
      </ul>
    </div>
  )
}

export default Document

