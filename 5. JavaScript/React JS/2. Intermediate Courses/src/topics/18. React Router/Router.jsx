import { Routes, Route} from 'react-router-dom'
import Home from './pages/Home'
import PostList from './pages/PostList'
import Post from './pages/Post'
import NewPost from './pages/NewPost'
import NotFound from './pages/NotFound'

import NavBar from './Components/NavBar'
import PostLayout from './Components/PostLayout'


const Router = () => {
  return (
    <>
        <NavBar />
        <Routes>
            <Route path='/' element={<Home />} />
            <Route path='/posts' element={ <PostLayout /> }>
                <Route index element={<PostList />} />
                <Route path='/posts/:id' element={<Post />} />
                <Route path='/posts/new' element={<NewPost />} />
            </Route>
            <Route path='*' element={<NotFound />} />
        </Routes>
    </>
  )
}

export default Router
