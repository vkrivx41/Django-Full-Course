import React, { useId } from 'react'
import useFetch from './Components/UseFetch'
import useLocalStorage from './Components/useLocalStorage'

const CustomHooks = () => {
  const id = useId()
  const data = useFetch("https://jsonplaceholder.typicode.com/todos")
  
  const [name, setName] = useLocalStorage('name', "")

  return (
    <>
    <div>
      <input type="text" value={ name } onChange={(e) => setName(e.target.value)} />
    </div>
    <ul>
        { data.slice(0, 10).map((item, index) => (
          <li key={ `${id}-${index}` }>{ item.title }</li>  
        )) }
    </ul>
    </>
  )
}

export default CustomHooks