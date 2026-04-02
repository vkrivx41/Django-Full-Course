import React from 'react'

const Grid = () => {
    return (
        <div className='grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 text-white p-6 gap-6 text-2xl text-center sm:text-sm'>
            <div className='bg-slate-500 rounded p-4 hover:bg-slate-600 hover:cursor-pointer hover:scale-105 transition-all duration-300'>Feature One</div>
            <div className='bg-slate-500 rounded p-4 hover:bg-slate-600 hover:cursor-pointer'>Feature Two</div>
            <div className='bg-slate-500 rounded p-4 hover:bg-slate-600 hover:cursor-pointer'>Feature Three</div>
            <div className='bg-slate-500 rounded p-4 hover:bg-slate-600 hover:cursor-pointer'>Feature Four</div>
            <div className='bg-slate-500 rounded p-4 hover:bg-slate-600 hover:cursor-pointer'>Feature Five</div>
            <div className='bg-slate-500 rounded p-4 hover:bg-slate-600 hover:cursor-pointer'>Feature Six</div>
        </div>
    )
}

export default Grid