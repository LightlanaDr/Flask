from pydantic import BaseModel, Field, EmailStr


class UserIn(BaseModel):
    username: str = Field(title="Имя")
    lastname: str = Field(title="Фамилия")
    email: EmailStr = Field(max_length=128)
    password: str = Field(min_length=6)


class User(BaseModel):
    user_id: int
    username: str = Field(title="Имя")
    lastname: str = Field(title="Фамилия")
    email:  EmailStr = Field(max_length=128)
