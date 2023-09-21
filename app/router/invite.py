from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from app.router.auth import token_auth_scheme, get_user_or_auth
from app.schemas.schema import Response, InviteBase, Invite, InviteCreate, RequestInvite, InviteUpdate, \
    RequestUpdateInvite, Company

from app import crud, invite_crud
from app.my_data.database import get_db

router3 = APIRouter()


@router3.post('/create/{user_id}/invite', response_model=Invite, status_code=201)
async def create_invite(invite: InviteCreate,
                        data: AsyncSession = Depends(get_db), token: str = Depends(token_auth_scheme)) -> Invite:
    _invite = await invite_crud.UserCrud(data).create_user_invite(
        user_email=await get_user_or_auth(db=data, token=token), invite=invite)

    if not _invite:
        raise HTTPException(status_code=404, detail="Invite is not created")
    return _invite


@router3.get("/invites/", response_model=List[Invite], status_code=201)
async def get_invites(skip: int = 0, limit: int = 100,
                      data: AsyncSession = Depends(get_db)) -> List[Invite]:
    _invite = await invite_crud.UserCrud(data).get_invites(skip, limit)
    if not _invite:
        raise HTTPException(status_code=404, detail="Invites are not found")
    return _invite


@router3.patch("/update", response_model=InviteUpdate, status_code=201)
async def update_invite(invite_id: int, request: RequestUpdateInvite,
                        data: AsyncSession = Depends(get_db),
                        token: str = Depends(token_auth_scheme)) -> Invite:
    _invite = await invite_crud.UserCrud(data).update_invite(invite_id=invite_id,
                                                             user=await get_user_or_auth(db=data, token=token),
                                                             confirm=request.parameter.confirm
                                                             )
    if _invite is None:
        raise HTTPException(status_code=404, detail="Invite is not updated")
    return _invite







