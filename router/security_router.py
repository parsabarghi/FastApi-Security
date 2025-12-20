from typing import Annotated
from fastapi import Depends, APIRouter
from service.security import oauth2_scheme

router = APIRouter()


@router.get("/sec")
async def sec(token: Annotated[str, Depends(oauth2_scheme)]):
    return {"sec": "healthy"}