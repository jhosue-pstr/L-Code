from fastapi import FastAPI
from config.database import *
from models.usuarios import *
from routers.users import *

app = FastAPI()


app.include_router(user)


@app.on_event("startup")
def on_startup():
    create_db_and_tables()