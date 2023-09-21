from typing import List

import passlib.hash as _hash
from sqlalchemy import select

from app.models.models import User, Company, Invite
from app.schemas import schema as schema
from app import crud


class UserCrud:

    def __init__(self, db):
        self.db = db

    # async def create_user_invite(self, invite: schema.InviteCreate, owner_email: str):
    #     db_invite = Invite(**invite.dict(), owner_email=owner_email)
    #     self.db.add(db_invite)
    #     await self.db.commit()
    #     await self.db.refresh(db_invite)
    #     return db_invite

    async def create_user_invite(self, invite: schema.InviteCreate, user_email: str) -> Invite:
        _invite = Invite(user_email=user_email, company_id=invite.company_id, user=invite.user)
        self.db.add(_invite)
        await self.db.commit()
        await self.db.refresh(_invite)
        return _invite

    async def get_invites(self, skip: int = 0, limit: int = 100) -> List[Invite]:
        invite = await self.db.execute(select(Invite).offset(skip).limit(limit))
        return invite.scalars().all()

    async def get_invite_by_id(self, invite_id: int, user: str) -> Invite:
        invite = await self.db.execute(
            select(Invite).filter(Invite.id == invite_id, Invite.user == user))
        return invite.scalars().first()

    # update without company only invite
    # async def update_invite(self, invite_id, user, confirm: bool) -> Invite:
    #     _invite = await self.get_invite_by_id(invite_id=invite_id, user=user)
    #     _invite.confirm = confirm
    #     await self.db.commit()
    #     await self.db.refresh(_invite)
    #     return _invite

    async def get_company_by_id(self, company_id: int, user_email: str) -> Company:
        company = await self.db.execute(
            select(Company).filter(Company.id == company_id, Company.owner_email == user_email))
        return company.scalars().first()

    async def update_invite(self, invite_id, user, confirm: bool) -> Invite:
        _invite = await self.get_invite_by_id(invite_id=invite_id, user=user)
        _invite.confirm = confirm
        # _company = await self.db.add(Company).values(users_emails=user).filter(Company.id == _invite.company_id)

        # _company = await self.get_company_by_id(company_id=_invite.company_id, user_email=_invite.user_email)
        # _company.users_emails = await self.db.add(user)
        await self.db.commit()
        await self.db.refresh(_invite)
        return _invite

