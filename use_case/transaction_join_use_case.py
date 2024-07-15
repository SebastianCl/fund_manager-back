from fastapi import HTTPException  # type: ignore
from schemas.transaction_join_schema import TransactionJoinSchema
from schemas.user_update_schema import UserUpdateSchema
from services.fund_service import FundService
from services.user_service import UserService
from services.transaction_service import TransactionService
from models.transaction_model import TransactionModel
from utils.utils import Utils
from utils.notification_sender import NotificationSender
from datetime import datetime
import logging

logger = logging.getLogger(__name__)


class TransactionJoinUseCase:

    def join_a_found(transactionJoin: TransactionJoinSchema) -> int:
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

            new_transaction_id = Utils.generate_unique_number()
            transactionService = TransactionService()
            transaction_join_data = TransactionModel(
                transaction_id=new_transaction_id,
                user_id=transactionJoin.user_id,
                fund_id=transactionJoin.fund_id,
                amount=transactionJoin.amount,
                type="apertura",
                date=datetime.now().isoformat(),
            )
            transactionService.create_transaction(transaction_join_data)

            new_amount = user_data.get("amount") - transactionJoin.amount
            new_user_data = UserUpdateSchema(
                amount=new_amount,
            )
            userService.update_user_amount(transactionJoin.user_id, new_user_data)

            to_phone = "+573012545154"

            to_email = "cardonaloaizasebastian112@gmail.com"
            subject = f"Suscrito al fondo: {fund_data.get('name')}"

            body = f"ID de la transacción: {new_transaction_id}"

            # Crear una instancia de NotificationSender
            notifier = NotificationSender()
            notifier.send_sms(to_phone, body)
            notifier.send_email(to_email, subject, body)

            return new_transaction_id

        except RuntimeError as e:
            logger.error(f"Error al registrar: {e}")
            raise HTTPException(status_code=500, detail="Error al registrar")
