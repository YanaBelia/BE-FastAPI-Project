from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from app.router.auth import token_auth_scheme, get_user_or_auth
from app.schemas.schema import  Response, Company, CompanyCreate, RequestUpdateCompany, CompanyDelete, CompanyUpdate


from app import crud
from app.my_data.database import get_db

router2 = APIRouter()


@router2.post('/create/{user_id}/company', response_model=Company, status_code=201)
async def create_company_user(company: CompanyCreate, data: AsyncSession = Depends(get_db),
                              token: str = Depends(token_auth_scheme)):
    _company = await crud.UserCrud(data).create_user_company(company=company,
                                                             user_email=await get_user_or_auth(db=data, token=token))
    if not _company:
        raise HTTPException(status_code=404, detail="Company is not created")
    return _company


@router2.get("/companies/", response_model=List[Company], status_code=201)
async def get_companies(skip: int = 0, limit: int = 100,
                        data: AsyncSession = Depends(get_db)) -> List[Company]:
    _company = await crud.UserCrud(data).get_companies(skip, limit)
    if not _company:
        raise HTTPException(status_code=404, detail="Companies are not found")
    return _company


@router2.delete("/{id}", response_model=CompanyDelete, status_code=201)
async def delete_company(company_id: int, data: AsyncSession = Depends(get_db),
                         token: str = Depends(token_auth_scheme)):
    try:
        await crud.UserCrud(data).remove_company(company_id=company_id,
                                                 user_email=await get_user_or_auth(db=data, token=token))
    except:
        raise HTTPException(status_code=404, detail="Company id not found")
    return Response(code="200", status="ok", message="Company deleted successfully").dict(exclude_none=True)


@router2.patch("/update", response_model=CompanyUpdate, status_code=201)
async def update_company(company_id: int, request: RequestUpdateCompany,
                         data: AsyncSession = Depends(get_db),
                         token: str = Depends(token_auth_scheme)) -> Company:
    _company = await crud.UserCrud(data).update_company(company_id=company_id,
                                                        user_email=await get_user_or_auth(db=data, token=token),
                                                        title=request.parameter.title,
                                                        description=request.parameter.description,
                                                        )
    if _company is None:
        raise HTTPException(status_code=404, detail="Company is not updated")
    return _company
