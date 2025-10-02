from sqlmodel import Field, SQLModel, Relationship
from typing import Optional, List
import datetime
from models import Usuario, Perfil


class UsuarioBase(SQLModel):
    Nombre: str
    Apellido: str
    Correo: str


class Usuario(UsuarioBase, table=True):
    IdUsuario: Optional[int] = Field(default=None, primary_key=True)
    Contrasena: str
    FechaRegistro: datetime.date = Field(default_factory=datetime.datetime.utcnow)
    estado: bool = True

    # Relación con Perfil (nota: usamos string "Perfil" en lugar de importarlo)
    perfiles: List["Perfil"] = Relationship(back_populates="usuario")


# Modelos Pydantic (para request/response)
class UsuarioCreate(UsuarioBase):
    Contrasena: str


class UsuarioPublic(UsuarioBase):
    IdUsuario: int
    FechaRegistro: datetime.date
    estado: bool


class UsuarioUpdate(SQLModel):
    Nombre: Optional[str] = None
    Apellido: Optional[str] = None
    Correo: Optional[str] = None
    Contrasena: Optional[str] = None
    estado: Optional[bool] = None
