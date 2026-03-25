import React from "react";

interface User {
  id: number
  name: string
  username: string
  address: object
}


const UserPage = async () => {
  const response = await fetch("https://jsonplaceholder.typicode.com/users")
  const data: User[] = await response.json()

  return (
    <div>
      <h1>Users</h1>
      <ul>
        {data.map(user => (
          <li key={user.id}>{user.username}</li>
        ))}
      </ul>
    </div>
  );
};

export default UserPage;
