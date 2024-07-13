from fastapi import APIRouter  # type: ignore
from fastapi.responses import JSONResponse  # type: ignore
from fastapi.encoders import jsonable_encoder  # type: ignore
from typing import List
from services.fund_service import FundService
from schemas.fund_schema import FundSchema

fund_router = APIRouter()


@fund_router.get(
    "/funds", tags=["funds"], response_model=List[FundSchema], status_code=200
)
def get_funds() -> List[FundSchema]:
    result = FundService.get_funds()
    return JSONResponse(status_code=200, content=jsonable_encoder(result))
