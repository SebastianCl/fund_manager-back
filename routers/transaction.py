from fastapi import APIRouter  # type: ignore
from fastapi.responses import JSONResponse  # type: ignore
from fastapi.encoders import jsonable_encoder  # type: ignore
from typing import List
from services.transaction import TransactionService
from schemas.transaction import Transaction

transaction_router = APIRouter()


@transaction_router.get("/transactions", tags=["transactions"], response_model=List[Transaction], status_code=200)
def get_transactions() -> List[Transaction]:
    result = TransactionService.get_transactions()
    return JSONResponse(status_code=200, content=jsonable_encoder(result))
