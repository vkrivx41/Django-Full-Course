import { useId } from 'react'

const Form = () => {
  const id = useId()

  console.log(document.querySelector("#_r_0_"))

  return (
    <form>
        <label htmlFor={ `email-${id}` }>Email:</label>
        <input type="email" name="email" id={ `email-${id}` } />
        <label htmlFor={ `name-${id}` }>Name:</label>
        <input type="name" name="name" id={ `name-${id}` } />
        </form>
  )
}

export default Form 