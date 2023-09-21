from typing import List

import passlib.hash as _hash
from sqlalchemy import select

from app.models.models import User, Company, Invite
from app.schemas import schema as schema


class UserCrud:

    def __init__(self, db):
        self.db = db

    async def get_users(self, skip: int = 0, limit: int = 100) -> List[User]:
        user = await self.db.execute(select(User).offset(skip).limit(limit))
        return user.scalars().all()

    async def get_user_by_id(self, user_id: int) -> User:
        user = await self.db.execute(select(User).filter(User.id == user_id))
        return user.scalars().first()

    async def create_user(self, user: schema.UserSchema) -> User:
        _user = User(password=_hash.bcrypt.hash(user.password), first_name=user.first_name, last_name=user.last_name,
                     email=user.email)
        self.db.add(_user)
        await self.db.commit()
        await self.db.refresh(_user)
        return _user

    async def remove_user(self, user_email):
        _user = await self.get_user_by_email(user_email=user_email)
        await self.db.delete(_user)
        await self.db.commit()

    async def update_user(self, user_email, password: str, first_name: str) -> User:
        _user = await self.get_user_by_email(user_email=user_email)
        _user.password = password
        _user.first_name = first_name
        await self.db.commit()
        await self.db.refresh(_user)
        return _user

    async def create_user_by_email(self, email: str, password: str, first_name: str, last_name: str) -> User:
        _user = User(email=email, password=_hash.bcrypt.hash(password),
                     first_name=first_name, last_name=last_name)
        self.db.add(_user)
        await self.db.commit()
        await self.db.refresh(_user)
        return _user

    async def get_user_by_email(self, user_email: str) -> User:
        user = await self.db.execute(select(User).filter(User.email == user_email))
        return user.scalars().first()

    async def create_user_company(self, company: schema.CompanyCreate, user_email: str):
        db_company = Company(**company.dict(), owner_email=user_email)
        self.db.add(db_company)
        await self.db.commit()
        await self.db.refresh(db_company)
        return db_company

    async def get_companies(self, skip: int = 0, limit: int = 100) -> List[Company]:
        company = await self.db.execute(select(Company).filter(Company.is_visible == True).offset(skip).limit(limit))
        return company.scalars().all()

    async def get_company_by_id(self, company_id: int, user_email: str) -> Company:
        company = await self.db.execute(
            select(Company).filter(Company.id == company_id, Company.owner_email == user_email))
        return company.scalars().first()

    async def remove_company(self, company_id, user_email):
        _company = await self.get_company_by_id(company_id=company_id, user_email=user_email)
        await self.db.delete(_company)
        await self.db.commit()

    async def update_company(self, company_id, user_email, title: str, description: str) -> Company:
        _company = await self.get_company_by_id(company_id=company_id, user_email=user_email)
        _company.title = title
        _company.description = description
        await self.db.commit()
        await self.db.refresh(_company)
        return _company

    # async def create_user_invite(self, invite: schema.InviteCreate, owner_email: str):
    #     db_invite = Invite(**invite.dict(), owner_email=owner_email)
    #     self.db.add(db_invite)
    #     await self.db.commit()
    #     await self.db.refresh(db_invite)
    #     return db_invite

    # async def create_user_invite(self, invite: schema.InviteCreate, user_email:str) -> Invite:
    #     _invite = User(user_email=user_email, company_id=invite.company_id)
    #     self.db.add(_invite)
    #     await self.db.commit()
    #     await self.db.refresh(_invite)
    #     return _invite

    # async def get_invites(self, user_email: str, skip: int = 0, limit: int = 100) -> List[Invite]:
    #     invite = await self.db.execute(select(Invite).filter(Invite.user_email == user_email).offset(skip).limit(limit))
    #     return invite.scalars().all()
