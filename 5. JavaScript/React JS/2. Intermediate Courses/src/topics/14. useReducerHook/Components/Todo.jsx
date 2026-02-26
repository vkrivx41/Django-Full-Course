import { useReducer, useState } from 'react'


class AddAction{
    constructor(todos){
        this.todos = todos
    }

    doAction(payload){
        return [...this.todos, newTodo(payload.name)]
    }
}

class DeleteAction{
    constructor(todos){
        this.todos = todos
    }

    doAction(payload){
        return this.todos.filter(todo => {
            if (todo.id !== payload.id){
                return todo
            }
        })
    }
}

class ToggleAction{
    constructor(todos){
        this.todos = todos
    }

    doAction(payload){
        return this.todos.map(todo => {
            if (todo.id === payload.id){
                return {...todo, completed: !todo.completed}
            }
            return todo
        })
    }
}

const reducer = (todos, {Action, payload}) => {
    const actor = new Action(todos)
    return actor.doAction(payload)
}

const newTodo = (name) => {
    return {
        id: Date.now(),
        name: name,
        completed: false
    }
}

const Todo = () => {
  const [todos, dispatch] = useReducer(reducer, [])
  const [name, setName] = useState("")

  const handleSubmit = (e) => {
    e.preventDefault()
   
    dispatch({
        Action: AddAction,
        payload: {name}
    })

    setName("")
  }

  return (
    <div>
        <h1>To Do List</h1>
        <form onSubmit={ handleSubmit }>
            <input type="text" value={ name } onChange={(e) => setName(e.target.value)} />
        </form>
        {todos.map(todo => (
            <div>
                <span style={{ color: todo.completed ? "#555" : "#000" }}>{ todo.name }</span>
                <button onClick={() => dispatch({Action: ToggleAction, payload: {id: todo.id}})}>Toggle</button>
                <button onClick={() => dispatch({Action: DeleteAction, payload: {id: todo.id}})}>Delete</button>
            </div>
        ))}
    </div>
  )
}

export default Todo