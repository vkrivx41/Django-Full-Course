import React, { useCallback, useState } from 'react'
import Header from './components/Header'


const Axios = () => {
    const [res, setRes] = useState(null)
    const [data, setData] = useState([])
    const [headers, setHeaders] = useState([])

    const setResponse = useCallback((response) => {
        console.log(response.config)

        const axiosHeaders = []
        for (const element of response.headers) {
            axiosHeaders.push({
                key: element[0],
                value: element[1],
            })
        }

        setRes(response)
        setHeaders(axiosHeaders)
        setData(() => {
            if (response.data.length) {
                return response.data
            }
            return [response.data]
        })
    }, [])

    return (
        <div>
            <Header setResponse={setResponse} />
            {res &&
                <div>
                    <h1 className="status">Status: {res.status}</h1>
                    <div className="headers">
                        <h1>Headers</h1>
                        {headers.map(hdr => (
                            <div key={Math.random()}>{hdr.key}: {hdr.value}</div>
                        ))}
                    </div>
                    <div className="data">
                        <h1>Data</h1>
                        {data.map(row => (
                            <div key={row.id}>{JSON.stringify(row)}</div>
                        ))}
                    </div>
                </div>
            }
        </div>
    )
}

export default Axios
