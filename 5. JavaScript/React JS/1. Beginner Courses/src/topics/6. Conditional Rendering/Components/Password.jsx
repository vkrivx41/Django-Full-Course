import React from 'react'

const IsValid = () => <h1>Valid Password</h1>
const IsInvalid = () => <h1>Invalid Password</h1>


const Password = ({ isValid }) => {
    // if (isValid) {
    //     return <IsValid />
    // }
    // return <IsInvalid />
    return isValid ? <IsValid /> : <IsInvalid />
}


export default Password