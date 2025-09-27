from fastapi import FastAPI
import os
from dotenv import load_dotenv
from sqlmodel import Field, Session, SQLModel, create_engine, select,text


load_dotenv()
db_user = os.getenv("USER_DB")
db_password = os.getenv("PASSWORD_DB")
db_host = os.getenv("HOST_DB")
db_port = os.getenv("PORT_DB")
db_name = os.getenv("NAME_DB")

url_connection = f"mysql+pymysql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}"
engine = create_engine(url_connection, echo=True)

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

