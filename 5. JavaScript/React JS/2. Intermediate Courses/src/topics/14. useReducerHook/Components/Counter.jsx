import React, { useState, useReducer } from 'react'


const ACTIONS = {
    INCREASE: "increase",
    DECREASE: "decrease",
    RESET: "reset",
}

const reducer = (state, action) => {
    switch (action.type) {
        case ACTIONS.INCREASE:
            return {...state, count: state.count + 1 }
        case ACTIONS.DECREASE:
            return {...state, count: state.count - 1 }
        case ACTIONS.RESET:
            if (state.count !== 0){
                return {
                    ...state,
                    count: 0,
                    resetCount: state.resetCount + 1,
                }
            }
            return state
            
        default:
            return state;
    }
}

const Counter = () => {
  const [state, dispatch] = useReducer(reducer, { count: 0, resetCount: 0 })

  return (
    <div>
        <h1>Count: { state.count }</h1>
        <h1>Resets: { state.resetCount }</h1>
        <button onClick={() => dispatch({ type: ACTIONS.INCREASE }) } >Increase</button>
        <button onClick={() => dispatch({ type: ACTIONS.DECREASE }) }>Decrease</button>
        <button onClick={() => dispatch({ type: ACTIONS.RESET }) }>Reset</button>
    </div>
  )
}

export default Counter
