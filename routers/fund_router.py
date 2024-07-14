from fastapi import APIRouter, Body  # type: ignore
from fastapi.responses import JSONResponse  # type: ignore
from fastapi.encoders import jsonable_encoder  # type: ignore
from typing import List
from services.fund_service import FundService
from schemas.fund_schema import FundSchema

fund_router = APIRouter()


@fund_router.get(
    "/funds",
    tags=["funds"],
    response_model=List[FundSchema],
    status_code=200,
)
def get_funds() -> FundSchema:
    fundService = FundService()
    result = fundService.get_funds()
    return JSONResponse(status_code=200, content=jsonable_encoder(result))


@fund_router.post("/funds", tags=["funds"], response_model=dict, status_code=201)
def create_fund(fund: FundSchema = Body()) -> dict:
    fundService = FundService()
    fundService.create_fund(fund)
    return JSONResponse(
        status_code=201, content={"message": "Se ha registrado el fondo"}
    )
