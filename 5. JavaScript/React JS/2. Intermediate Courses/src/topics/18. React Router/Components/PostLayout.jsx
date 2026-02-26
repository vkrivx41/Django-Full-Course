import React from 'react'
import { Link, Outlet } from 'react-router-dom'


const PostLayout = () => {
  return (
    <div>
        <div>
            <Link to="/posts/1">Post 1</Link>
        </div>
        <div>
            <Link to="/posts/2">Post 2</Link>
        </div>
        <div>
            <Link to="/posts/new">New Post</Link>
        </div>
        <Outlet />
    </div>
  )
}

export default PostLayout   