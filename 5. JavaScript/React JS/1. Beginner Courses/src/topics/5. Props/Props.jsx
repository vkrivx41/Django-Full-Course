import React from 'react'
import User from './Components/User'
import Product from './Components/Product'
import Article from './Components/Article'


const Props = () => {
  return (
    <div>
        <User
          name="Scorpus"
          age={ 21 }
          hobbies={ ["Coding", "Reading", "Working Out"] }
          isMarried={ false }
        />
        <Product name="Samsung Galaxy S25 Ultra" price={ 1250 } />
        <Article>
          <h1 className="title">
            The Title of the Article
          </h1>
          <p>The body of the article, Lorem ipsum dolor sit amet consectetur, adipisicing elit. Accusamus, itaque!</p>
        </Article>
        <Article>
          <h1 className="title">
            The Title of the Article
          </h1>
          <p>The body of the article, Lorem ipsum dolor sit amet consectetur, adipisicing elit. Accusamus, itaque!</p>
        </Article>
    </div>
  )
}

export default Props
