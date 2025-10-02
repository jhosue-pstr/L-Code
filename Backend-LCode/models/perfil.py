from sqlmodel import Field, SQLModel, Relationship
from typing import Optional
from models import Usuario, Perfil



class PerfilBase(SQLModel):
    foto: Optional[str] = None


class Perfil(PerfilBase, table=True):
    IdPerfil: Optional[int] = Field(default=None, primary_key=True)
    Descripcion: str
    rol: str
    IdUsuario: Optional[int] = Field(default=None, foreign_key="usuario.IdUsuario")

    # Relación inversa con Usuario (nota: usamos string "Usuario")
    usuario: Optional["Usuario"] = Relationship(back_populates="perfiles")


# Modelos Pydantic (para request/response)
class PerfilCreate(PerfilBase):
    Descripcion: str
    rol: str
    IdUsuario: int   # aquí solo se recibe, no se define FK


class PerfilPublic(PerfilBase):
    IdPerfil: int
    Descripcion: str
    rol: str
    IdUsuario: int


class PerfilUpdate(SQLModel):
    foto: Optional[str] = None
    Descripcion: Optional[str] = None
