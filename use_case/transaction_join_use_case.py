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

    def __init__(self):
        self.user_service = UserService()
        self.fund_service = FundService()
        self.transaction_service = TransactionService()
        self.notifier = NotificationSender()

    def join_a_fund(self, transaction_join: TransactionJoinSchema) -> int:
        user_data = self.user_service.get_user(transaction_join.user_id)

        if not user_data:
            logger.warning(f"Usuario no encontrado: {transaction_join.user_id}")
            raise HTTPException(status_code=404, detail="Usuario no encontrado")

        if transaction_join.amount > user_data.get("amount"):
            raise HTTPException(status_code=400, detail="Saldo insuficientes")

        fund_data = self.fund_service.get_fund(transaction_join.fund_id)
        if not fund_data:
            logger.warning(f"Fondo no encontrado: {transaction_join.fund_id}")
            raise HTTPException(status_code=404, detail="Fondo no encontrado")

        if transaction_join.amount < fund_data.get("minimum_amount"):
            raise HTTPException(
                status_code=400,
                detail=f"No tiene saldo disponible para vincularse al fondo "
                + fund_data.get("name"),
            )

        new_transaction_id = Utils.generate_unique_number()
        transaction_data = TransactionModel(
            transaction_id=new_transaction_id,
            user_id=transaction_join.user_id,
            fund_id=transaction_join.fund_id,
            amount=transaction_join.amount,
            type="apertura",
            date=datetime.now().isoformat(),
        )
        self.transaction_service.create_transaction(transaction_data)

        new_amount = user_data.get("amount") - transaction_join.amount
        user_update_data = UserUpdateSchema(amount=new_amount)
        self.user_service.update_user_amount(transaction_join.user_id, user_update_data)

        self._send_notification(
            transaction_join, user_data, new_transaction_id, fund_data
        )

        return new_transaction_id

    def _send_notification(
        self,
        transaction_join: TransactionJoinSchema,
        user_data,
        transaction_id: int,
        fund_data,
    ):
        body = f"ID de la transaction: {transaction_id}"

        if transaction_join.notification == "email":
            to_email = user_data.get("email")
            subject = f"Suscrito al fondo: {fund_data.get('name')}"
            self.notifier.send_email(to_email, subject, body)
        else:
            to_phone = user_data.get("phone")
            self.notifier.send_sms(to_phone, body)
