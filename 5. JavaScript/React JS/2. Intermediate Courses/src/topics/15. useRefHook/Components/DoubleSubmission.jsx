import { useState, useRef, use } from 'react'

const DoubleSubmission = () => {
  const [status, setStatus] = useState('idle')
  const isSubmitting = useRef(false)

  const handleSubmit = async () => {
    if (isSubmitting.current){
        alert("Can't double submit")
        return
    }

    isSubmitting.current = true
    setStatus('submitting')

    try {
        for (let i = 0; i < 10; i++) {
            await fetch('https://jsonplaceholder.typicode.com/todos/', {method: 'GET'})
        }
        setStatus('success')
    } catch (error) {
        setStatus('error')
    } finally{
        isSubmitting.current = false
    }
  }

  return (
    <div>
        <hr />
        <h1>We don't allow double submission</h1>
        <button onClick={ handleSubmit } disabled={ status === 'submitting' }>
            { status == 'submitting' ? "Submitting" : "Submit" }
        </button>
    </div>
  )
}

export default DoubleSubmission