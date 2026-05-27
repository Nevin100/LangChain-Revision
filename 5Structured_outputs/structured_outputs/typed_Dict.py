from typing import TypedDict

# Define a TypedDict for a user
class User(TypedDict):
    name: str
    age: int
    email: str
    
# Create a new user using the TypedDict
new_user: User = {
    "name": "John Doe",
    "age": 30,
    "email": "john.doe@example.com"
}

print(new_user)