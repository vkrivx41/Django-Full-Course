import React, { useEffect, useState } from 'react'

const Data = () => {
  const [todos, setTodos] = useState(() => [])

  useEffect(() => {
    const getData = () => {
      const response = localStorage.getItem('todos')
      const data = JSON.parse(response)

      if (data && data.length > 0){
        setTodos(data)
      }

    }

    getData()
  }, [])

  
  return (
    <div>
      <ol>
        { todos.map(todo => (
          <li key={ Math.random() }>{ todo.name } - { todo.created_at }</li>
        )) }
      </ol>
    </div>
  )
}

export default Data
