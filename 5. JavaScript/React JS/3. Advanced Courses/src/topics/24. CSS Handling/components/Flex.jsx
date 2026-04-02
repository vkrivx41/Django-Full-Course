import React from 'react'

const Flex = () => {
    return (
        <div className='flex items-center justify-between h-[50px] bg-slate-800 px-4'>
            <div className='text-3xl font-bold text-white'>LOGO</div>
            <div className='flex items-center gap-2 text-white'>
                <div>Home</div>
                <div>About</div>
                <div>Contact</div>
            </div>
        </div>
    )
}

export default Flex