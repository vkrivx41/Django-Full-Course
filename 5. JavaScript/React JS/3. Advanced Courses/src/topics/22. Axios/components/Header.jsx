import React from 'react'

import axios from 'axios'


// api
const api = axios.create({
    baseURL: "https://jsonplaceholder.typicode.com/"
})

// axios globals
api.defaults.baseURL = "https://jsonplaceholder.typicode.com/"
api.defaults.headers.common["X-Authorization-Token"] = "sometoken"

// interceptors
// request
api.interceptors.request.use(
    (config) => {
        const accessToken = localStorage.getItem("access_token")

        if (accessToken) {
            config.headers["Authorization"] = "Bearer " + accessToken
        }

        config.timeout = 5000

        return config
    },
    (error) => {
        Promise.reject(error)
    })

// response 
api.interceptors.response.use(
    (res) => {
        console.log("Response: ", res)
        return res
    },
    (error) => {
        if (error.response?.status == 401) {
            console.log("Unauthorized -> Refresh the token")
        }
        Promise.reject(error)
    })



const Header = ({ setResponse }) => {
    console.log("re-render")

    const getRequest = () => {
        // api({
        //     method: "GET",
        //     url: "https://jsonplaceholder.typicode.com/todos"
        // })
        //     .then(res => setResponse(res))
        //     .catch(err => console.error(err))

        api.get("/todos")
            .then(res => setResponse(res))
            .catch(err => console.error(err))
    }

    const postRequest = () => {
        api.post("https://jsonplaceholder.typicode.com/todos", {
            title: "New Todo",
            completed: false
        })
            .then(res => setResponse(res))
            .catch(err => console.error(err))
    }

    const putOrPatchRequest = () => {
        api.patch("https://jsonplaceholder.typicode.com/todos/1", {
            title: "Updated Todo",
            completed: true
        })
            .then(res => setResponse(res))
            .catch(err => console.error(err))
    }

    const deleteRequest = () => {
        api.delete("https://jsonplaceholder.typicode.com/todos/1")
            .then(res => setResponse(res))
            .catch(err => console.error(err))
    }

    const simRequests = () => {
        // api.all([
        //     api.get("https://jsonplaceholder.typicode.com/todos/1"),
        //     api.patch("https://jsonplaceholder.typicode.com/todos/2", {
        //         title: "Updated Todo",
        //         completed: true
        //     }),
        // ])
        //     .then(([res1, res2]) => setResponse(res2))
        //     .catch(err => console.error(err))

        Promise.all([
            api.get("https://jsonplaceholder.typicode.com/todos/1"),
            api.patch("https://jsonplaceholder.typicode.com/todos/2", {
                title: "Updated Todo",
                completed: true
            })
        ])
            .then(([res1, res2]) => setResponse(res2))
            .catch(err => console.error(err))
    }

    const customHeaders = () => {
        const config = {
            headers: {
                "Content-Type": "application/json",
                Authorization: "Bearer sometoken"
            },
            timeout: 2000
        }

        api.post("https://jsonplaceholder.typicode.com/todos", {
            title: "New Todo",
            completed: false,
        },
            config
        )
            .then((res) => setResponse(res))
            .catch(err => console.error(err))
    }

    const errorHandling = () => {
        const config = {
            headers: {
                "Content-Type": "application/json",
                Authorization: "Bearer sometoken"
            },
            timeout: 2000
        }

        api.post("/postss", {
            title: "New Post",
            description: "The description"
        },
            config
        )
            .then((res) => setResponse(res))
            .catch(err => {
                if (err.response) {
                    // Request was made but server responded with a status not in the 200 range
                    console.log(err.response)
                    setResponse(err.response)
                } else if (err.request) {
                    // Request was made but not response from the server (ex: timeout)
                    console.log(err.request)
                } else {
                    console.log(err.message)
                }
            })
    }

    const progress = () => {
        api.post("/comments", {
            title: "New Todo",
            completed: false
        }, {
            onUploadProgress: (progressEvent) => {
                const completed = Math.round(progressEvent.loaded / progressEvent.total) * 100
                console.log(`Uploaded: ${completed}%`)
            }
        })
            .then(res => setResponse(res))
            .catch(err => console.error(err))
    }


    return (
        <div>
            <button onClick={() => getRequest()}>GET</button>
            <button onClick={() => postRequest()}>POST</button>
            <button onClick={() => putOrPatchRequest()}>PUT/PATCH</button>
            <button onClick={() => deleteRequest()}>DELETE</button>
            <button onClick={() => simRequests()}>Sim Requests</button>
            <button onClick={() => customHeaders()}>Custom Headers</button>
            <button onClick={() => errorHandling()}>Error Handling</button>
            <button onClick={() => progress()}>Progress</button>
        </div>
    )
}

export default React.memo(Header)