from typing import Annotated

from fastapi import Depends, FastAPI, HTTPException, Query
from sqlmodel import Field, Session, SQLModel, create_engine, select
import datetime



class Usuarios(SQLModel , table=True):
    IdUsuario: Annotated[int | None, Field(primary_key=True)] = None
    Nombre: str
    Apellido: str
    Correo: str
    Contrasena: str
    FechaRegistro: str|datetime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    estado: bool = True



def create_db_and_tables():
    SQLModel.metadata.create_all(engine)    