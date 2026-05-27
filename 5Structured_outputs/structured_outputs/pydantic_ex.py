from pydantic import BaseModel

# Define a User model using Pydantic
class User(BaseModel):
    id: int
    name: str
    email: str

# Create an instance of the User model    
user : User = User(id=1, name="John Doe", email="john.doe@example.com")

# Print the user instance
print(user)