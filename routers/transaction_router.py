from fastapi import APIRouter, Body  # type: ignore
from fastapi.responses import JSONResponse  # type: ignore
from fastapi.encoders import jsonable_encoder  # type: ignore
from typing import List
from services.transaction_service import TransactionService
from schemas.transaction_schema import TransactionSchema
from schemas.transaction_join_schema import TransactionJoinSchema
from use_case.transaction_join_use_case import TransactionJoinUseCase

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

@transaction_router.post(
    "/join_a_found", tags=["transactions"], response_model=dict, status_code=201
)
def join_a_found(transactionJoin: TransactionJoinSchema = Body()) -> dict:
    TransactionJoinUseCase.join_a_found(transactionJoin)
    return JSONResponse(
        status_code=201, content={"message": "Se ha registrado la transacción"}
    )
