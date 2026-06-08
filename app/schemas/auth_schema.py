from pydantic import BaseModel, EmailStr , Field

class RegisterSchema(BaseModel):
    name: str
    email: EmailStr
    phone: str
    password: str = Field(max_length=72) 
   
class LoginSchema(BaseModel):
    
    email: EmailStr
    password: str