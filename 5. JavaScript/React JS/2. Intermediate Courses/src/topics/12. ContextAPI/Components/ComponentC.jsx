import React from 'react'

import { Data, MoreData } from './../ContextAPI'

const ComponentC = () => {
  return (
    <Data.Consumer>
        { (name) => {
            return <MoreData.Consumer>
                {(age) => {
                    return <h1>My name is { name }, I'm { age }.</h1>
                }}
            </MoreData.Consumer>
        }}
    </Data.Consumer>
  )
}

export default ComponentC