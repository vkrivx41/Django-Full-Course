import React from 'react'
import Portal from './topics/10. Portal/Portal'
import UseEffectHook from './topics/11. useEffectHook/useEffectHook'
import ContextAPI from './topics/12. ContextAPI/ContextAPI'
import UseContextHook from './topics/13. useContextHook/useContextHook'
import UseReducerHook from './topics/14. useReducerHook/UseReducerHook'
import UseRefHook from './topics/15. useRefHook/UseRefHook'
import UseIdHook from './topics/16. useIdHook/UseIdHook'
import CustomHooks from './topics/17. Custom Hooks/CustomHooks'
import Router from './topics/18. React Router/Router'
import { BrowserRouter } from 'react-router-dom'


const App = () => {
  return (
    <BrowserRouter>
      <Router />
    </BrowserRouter>
  )
}

export default App
