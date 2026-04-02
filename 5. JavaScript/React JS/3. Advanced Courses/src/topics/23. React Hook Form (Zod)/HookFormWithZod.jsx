import React from 'react'
import { useForm } from 'react-hook-form'

import WithoutZod from './components/WithoutZod'
import WithZod from './components/WithZod'

const HookFormWithZod = () => {
    return (
        <>
            <WithoutZod />
            <WithZod />
        </>
    )
}

export default HookFormWithZod