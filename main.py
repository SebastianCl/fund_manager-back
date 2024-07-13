import os
from dotenv import load_dotenv  # type: ignore
from fastapi import FastAPI  # type: ignore

from middlewares.error_handler import ErrorHandler

from routers.fund import fund_router
from routers.transaction import transaction_router

load_dotenv()

app = FastAPI()
version = os.getenv("VERSION")

app.title = "Fund Manager"
app.version = version

app.add_middleware(ErrorHandler)

app.include_router(fund_router)
app.include_router(transaction_router)


@app.get("/", tags=["home"])
def home():
    return f"Versión: " + version
