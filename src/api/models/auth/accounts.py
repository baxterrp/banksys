from typing import Annotated

from pydantic import BaseModel, EmailStr, Field, SecretStr

NonEmptyStr = Annotated[str, Field(min_length=1, max_length=255)]
PasswordStr = Annotated[SecretStr, Field(min_length=8, max_length=128)]

class RegistrationRequest(BaseModel):
    email: EmailStr
    password: PasswordStr
    first_name: NonEmptyStr
    last_name: NonEmptyStr

class LoginModel(BaseModel):
    email: EmailStr
    password: SecretStr