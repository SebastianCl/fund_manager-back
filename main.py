import os
import logging
from dotenv import load_dotenv  # type: ignore
from fastapi import FastAPI  # type: ignore

from middlewares.error_handler import ErrorHandler

from routers.fund_router import fund_router
from routers.transaction_router import transaction_router

load_dotenv()
logging.basicConfig(level=logging.INFO)

app = FastAPI()
version = os.getenv("VERSION")

app.title = "Fund Manager"
app.version = version

app.add_middleware(ErrorHandler)

app.include_router(fund_router)
app.include_router(transaction_router)
