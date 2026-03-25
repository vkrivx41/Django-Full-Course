import React, { useState } from 'react'

const ToDoList = () => {
  const [todos, setTodos] = useState(() => {
    const items = localStorage.getItem('todos')
    return items ? JSON.parse(items) : []
  })
  const [todoName, setTodoName] = useState("")

  const handleSubmit = (e) => {
    e.preventDefault()

    if (todoName === "") return

    setTodos(prevTodos => {
        const items = [...prevTodos, {
            'name': todoName,
            'created_at': new Date().toUTCString()
        }]
        localStorage.setItem('todos', JSON.stringify(items))

        return items
    })

    setTodoName(() => "")
  }

  const handleNameChange = (e) => setTodoName(e.target.value)

  return (
    <div>
        <h1>To Do List</h1>
        <form onSubmit={ handleSubmit }>
            <input type="text" onChange={ handleNameChange } value={ todoName } />
            <button type="submit">Add</button>
        </form>
        <ol>
            { todos.map(todo => (
                <li key={ Math.random() }> { todo.name } - {todo.created_at }</li>
            )) }
        </ol>
    </div>
  )
}

export default ToDoList
