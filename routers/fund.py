from fastapi import APIRouter  # type: ignore
from fastapi.responses import JSONResponse  # type: ignore
from fastapi.encoders import jsonable_encoder  # type: ignore
from typing import List
from services.fund import FundService
from schemas.fund import Fund

fund_router = APIRouter()


@fund_router.get("/funds", tags=["funds"], response_model=List[Fund], status_code=200)
def get_funds() -> List[Fund]:
    result = FundService.get_funds()
    return JSONResponse(status_code=200, content=jsonable_encoder(result))
