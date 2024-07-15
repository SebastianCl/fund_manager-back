from fastapi import HTTPException  # type: ignore
from schemas.transaction_join_schema import TransactionJoinSchema
from schemas.transaction_cancel_schema import TransactionCancelSchema
from schemas.user_update_schema import UserUpdateSchema
from services.user_service import UserService
from services.transaction_service import TransactionService
from models.transaction_model import TransactionModel
from utils.utils import Utils
from datetime import datetime
import logging

logger = logging.getLogger(__name__)


class TransactionCancelUseCase:

    def cancel_a_found(transactionCancel: TransactionCancelSchema) -> int:

        try:
            transactionService = TransactionService()
            transaction_data = transactionService.get_transaction(
                transactionCancel.transaction_id
            )
            if not transaction_data:
                raise HTTPException(status_code=404, detail="No existe el registro")

            userService = UserService()
            user_data = userService.get_user(transaction_data.get("user_id"))

            if not user_data:
                raise HTTPException(status_code=404, detail="No existe el usuario")

            new_transaction_id = Utils.generate_unique_number()

            transaction_cancel_data = TransactionModel(
                transaction_id=new_transaction_id,
                user_id=transaction_data.get("user_id"),
                fund_id=transaction_data.get("fund_id"),
                amount=transaction_data.get("amount"),
                type="cancelacion",
                date=datetime.now().isoformat(),
            )
            transactionService.create_transaction(transaction_cancel_data)

            new_amount = user_data.get("amount") + transaction_data.get("amount")
            new_user_data = UserUpdateSchema(
                amount=new_amount,
            )
            userService.update_user_amount(
                transaction_data.get("user_id"), new_user_data
            )
            return new_transaction_id

        except RuntimeError as e:
            logger.error(f"Error al registrar: {e}")
            raise HTTPException(status_code=500, detail="Error al registrar")
