from fastapi import HTTPException  # type: ignore
from schemas.transaction_join_schema import TransactionJoinSchema
from schemas.user_update_schema import UserUpdateSchema
from services.fund_service import FundService
from services.user_service import UserService
from services.transaction_service import TransactionService
from models.transaction_model import TransactionModel
from utils.utils import Utils
from datetime import datetime
import logging

logger = logging.getLogger(__name__)


class TransactionJoinUseCase:

    def join_a_found(transactionJoin: TransactionJoinSchema):

        try:
            userService = UserService()
            user_data = userService.get_user(transactionJoin.user_id)

            if not user_data:
                raise HTTPException(status_code=404, detail="No existe el usuario")

            if transactionJoin.amount > user_data.get("amount"):
                raise HTTPException(status_code=400, detail="Fondos insuficientes")

            fundService = FundService()
            fund_data = fundService.get_fund(transactionJoin.fund_id)
            if not fund_data:
                raise HTTPException(status_code=404, detail="No existe el fondo")

            if transactionJoin.amount < fund_data.get("minimum_amount"):
                raise HTTPException(
                    status_code=400,
                    detail=f"No tiene saldo disponible para vincularse al fondo "
                    + fund_data.get("name"),
                )

            transactionService = TransactionService()
            transaction_data = TransactionModel(
                transaction_id=Utils.generar_numero_unico(),
                fund_id=transactionJoin.fund_id,
                amount=transactionJoin.amount,
                type="apertura",
                date=datetime.now().isoformat(),
            )
            transactionService.create_transaction(transaction_data)

            new_amount = user_data.get("amount") - transactionJoin.amount
            new_user_data = UserUpdateSchema(
                amount=new_amount,
            )
            userService.update_user_amount(transactionJoin.user_id, new_user_data)

        except RuntimeError as e:
            logger.error(f"Error al registrar: {e}")
            raise HTTPException(status_code=500, detail="Error al registrar")
