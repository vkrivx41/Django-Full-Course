function Greeting() {
    let username = "Nik"
    let date = new Date()

    return (
        <div>
            <h1>Hello { username } </h1>
            <p>Today is: { date.toLocaleDateString('en-UK') }</p>
        </div>
    )
}

export default Greeting
