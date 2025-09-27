from typing import Annotated
from fastapi import Depends, HTTPException, Query
from sqlmodel import Field, Session, SQLModel, create_engine, select
import datetime
from config.database import engine

class Usuario(SQLModel, table=True):
    IdUsuario: Annotated[int | None, Field(primary_key=True)] = None
    Nombre: str
    Apellido: str
    Correo: str
    Contrasena: str
    FechaRegistro: str
    estado: bool = True

