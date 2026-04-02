import React, { lazy } from 'react'
import wait from './wait'

export default function lazyLoad(path, namedExport) {
    console.log(path, namedExport)
    return lazy(() => {
        const promise = wait(1000).then(() => import(path))

        if (namedExport) {
            return promise.then(module => {
                return { default: module[namedExport] }
            })
        }

        return promise
    })
}
