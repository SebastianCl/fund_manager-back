from fastapi import APIRouter, Body  # type: ignore
from fastapi.responses import JSONResponse  # type: ignore
from fastapi.encoders import jsonable_encoder  # type: ignore
from typing import List
from services.transaction_service import TransactionService
from schemas.transaction_schema import TransactionSchema

transaction_router = APIRouter()


@transaction_router.get(
    "/transactions",
    tags=["transactions"],
    response_model=List[TransactionSchema],
    status_code=200,
)
def get_transactions() -> TransactionSchema:
    transactionService = TransactionService()
    result = transactionService.get_transactions()
    return JSONResponse(status_code=200, content=jsonable_encoder(result))


@transaction_router.post(
    "/transactions", tags=["transactions"], response_model=dict, status_code=201
)
def create_transaction(transaction: TransactionSchema = Body()) -> dict:
    transactionService = TransactionService()
    transactionService.create_transaction(transaction)
    return JSONResponse(
        status_code=201, content={"message": "Se ha registrado la transacción"}
    )
