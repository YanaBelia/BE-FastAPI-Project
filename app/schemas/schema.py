from datetime import datetime
from typing import Optional, Generic, TypeVar, List

from pydantic import BaseModel, Field
from pydantic.generics import GenericModel

T = TypeVar('T')


class CompanyDelete(BaseModel):
    id: Optional[int] = None
    title: Optional[str] = None
    description: Optional[str] = None
    is_visible: Optional[bool] = None
    owner_email: Optional[str] = None

    class Config:
        orm_mode = True


class CompanyUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None

    class Config:
        orm_mode = True


class CompanyBase(BaseModel):
    title: str
    description: str
    is_visible: bool
    # owner_id: Optional[int] = Field(default=None, foreign_key="user.id")
    # owner_id: int


class CompanyCreate(CompanyBase):
    pass


class Company(CompanyBase):
    id: int
    owner_email: str

    class Config:
        orm_mode = True


class RequestCompany(BaseModel):
    parameter: Company = Field(...)


class UserSchema(BaseModel):
    id: Optional[int] = None
    password: Optional[str] = None
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    email: Optional[str] = None

    # company: List[Company] = []

    class Config:
        orm_mode = True


class InviteBase(BaseModel):
    user_email: str
    company_id: int
    user: str


class InviteCreate(InviteBase):
    pass


class Invite(InviteBase):
    id: int
    user_email: str
    user: str

    class Config:
        orm_mode = True


class InviteUpdate(BaseModel):
    confirm: Optional[bool] = None

    class Config:
        orm_mode = True


class UpdateUser(BaseModel):
    id: Optional[int] = None
    password: Optional[str] = None
    first_name: Optional[str] = None
    last_name: Optional[str] = None

    class Config:
        orm_mode = True


class UserId(BaseModel):
    id: Optional[int] = None

    class Config:
        orm_mode = True


class CompanyBase(BaseModel):
    title: str
    description: str
    is_visible: bool


class Request(GenericModel, Generic[T]):
    parameter: Optional[T] = Field(...)


class RequestUser(BaseModel):
    parameter: UserSchema = Field(...)


class RequestInvite(BaseModel):
    parameter: InviteCreate = Field(...)


class RequestUserId(BaseModel):
    parameter: UserId = Field(...)


class RequestUpdateUser(BaseModel):
    parameter: UpdateUser = Field(...)


class RequestUpdateCompany(BaseModel):
    parameter: CompanyUpdate = Field(...)


class RequestUpdateInvite(BaseModel):
    parameter: InviteUpdate = Field(...)


class Response(GenericModel, Generic[T]):
    code: str
    status: str
    message: str
    result: Optional[T]
