import React, { useState } from 'react'

const Themes = () => {
    const [mobileOpen, setMobileOpen] = useState(false)
    const [theme, setTheme] = useState("light")

    const openMobile = () => {
        setMobileOpen(current => !current)
    }

    const toggleTheme = () => {
        setTheme(current => current == "light" ? "dark" : "light")
    }

    return (
        <div className={`${theme} min-h-screen text-slate-900 dark:text-white dark:bg-slate-900`}>
            <div className='flex items-center justify-between h-[50px] px-4 bg-slate-200 dark:bg-background'>
                <div className='text-3xl font-bold text-slate-900 dark:text-white'>LOGO</div>
                <div className='hidden sm:flex items-center gap-2 text-slate-900 dark:text-white'>
                    <div>Home</div>
                    <div>About</div>
                    <div>Contact</div>
                    <button onClick={() => toggleTheme()}>
                        {theme == "light" ? "🌙" : "☀️"}
                    </button>
                </div>
                <button className='text-slate-900 dark:text-white text-2xl cursor-pointer sm:hidden' onClick={() => openMobile()}>Ξ</button>
            </div>
            {mobileOpen &&
                <div className='flex flex-col items-center gap-2 p-4 bg-slate-200 text-slate-900 sm:hidden dark:text-white dark:bg-slate-900'>
                    <div>Home</div>
                    <div>About</div>
                    <div>Contact</div>
                    <button onClick={() => toggleTheme()}>
                        {theme == "light" ? "🌙" : "☀️"}
                    </button>
                </div>
            }
            <div className='grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 p-6 gap-6 text-2xl text-center sm:text-sm text-white dark:bg-slate-900 dark:text-slate-white'>
                <div className='bg-slate-500 rounded p-4 hover:bg-slate-600 hover:cursor-pointer hover:scale-105 transition-all duration-300'>Feature One</div>
                <div className='bg-slate-500 rounded p-4 hover:bg-slate-600 hover:cursor-pointer'>Feature Two</div>
                <div className='bg-slate-500 rounded p-4 hover:bg-slate-600 hover:cursor-pointer'>Feature Three</div>
                <div className='bg-slate-500 rounded p-4 hover:bg-slate-600 hover:cursor-pointer'>Feature Four</div>
                <div className='bg-slate-500 rounded p-4 hover:bg-slate-600 hover:cursor-pointer'>Feature Five</div>
                <div className='bg-slate-500 rounded p-4 hover:bg-slate-600 hover:cursor-pointer'>Feature Six</div>
            </div>
        </div>
    )
}

export default Themes