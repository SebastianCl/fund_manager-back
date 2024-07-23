import os
import logging
from dotenv import load_dotenv  # type: ignore
from fastapi import FastAPI  # type: ignore
from fastapi.middleware.cors import CORSMiddleware  # type: ignore

from middlewares.error_handler import ErrorHandler

from routers.fund_router import fund_router
from routers.transaction_router import transaction_router
from routers.user_router import user_router

load_dotenv()
logging.basicConfig(level=logging.INFO)

app = FastAPI()
version = os.getenv("VERSION")

app.title = "Fund Manager"
app.version = version

app.add_middleware(ErrorHandler)

app.include_router(fund_router)
app.include_router(transaction_router)
app.include_router(user_router)

origins = [
    "http://localhost:3000",
    "http://fund-manager-front.s3-website.us-east-2.amazonaws.com",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
