import React, { useContext, useEffect, useState } from 'react'

import { MeContext } from './context/MeContext'
import Document from './components/Document'

const App = () => {
  return (
    <MeContext>
        <Document />
    </MeContext>
  )
}

export default App