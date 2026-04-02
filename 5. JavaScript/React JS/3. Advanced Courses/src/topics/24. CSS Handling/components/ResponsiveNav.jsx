import React, { useState } from 'react'

const ResponsiveNav = () => {
    const [mobileOpen, setMobileOpen] = useState(false)

    const openMobile = () => {
        setMobileOpen(current => !current)
    }

    return (
        <>
            <div className='flex items-center justify-between h-[50px] bg-slate-800 px-4'>
                <div className='text-3xl font-bold text-white'>LOGO</div>
                <div className='hidden sm:flex items-center gap-2 text-white'>
                    <div>Home</div>
                    <div>About</div>
                    <div>Contact</div>
                </div>
                <button className='text-white text-2xl cursor-pointer sm:hidden' onClick={() => openMobile()}>Ξ</button>
            </div>
            {mobileOpen &&
                <div className='flex flex-col items-center gap-2 text-white bg-slate-800 p-4'>
                    <div>Home</div>
                    <div>About</div>
                    <div>Contact</div>
                </div>
            }
        </>
    )
}

export default ResponsiveNav