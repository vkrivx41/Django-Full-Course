export default function WelcomeMessage() {
  return (
    <>
        <h2>Hello, World</h2>
        <p className='paragraph'>Welcome To Learning JSX.</p>
        <form action='#' method="post">
            <label htmlFor="username">Username:</label>
            <input type="text" placeholder='Enter username' />
            <button type="submit">Enter</button>
        </form>
    </>
  )
}