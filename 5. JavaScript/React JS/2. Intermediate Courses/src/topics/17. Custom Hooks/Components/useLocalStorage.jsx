import React, { useEffect, useState } from 'react'

const getSetData = (key, initialValue) => {
  const items = localStorage.getItem(key)

  if (items){
    if (items.includes("[") || items.includes("{")){
      const data = JSON.parse(items)
      return data
    }
    return items
  }

  if (initialValue instanceof Function) return initialValue()
  return initialValue
}


const useLocalStorage = (key, initialValue) => {
  const [value, setValue] = useState(() => {
    return getSetData(key, initialValue)
  })

  useEffect(() => {
    localStorage.setItem(key, value)
  }, [value])

  return [value, setValue]
}

export default useLocalStorage
