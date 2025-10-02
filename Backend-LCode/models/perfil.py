from sqlmodel import Field, SQLModel, Relationship
from typing import Optional

class PerfilBase(SQLModel):
    foto: Optional[str] = None

class Perfil(PerfilBase, table=True):
    IdPerfil: Optional[int] = Field(default=None, primary_key=True)
    Descripcion: str
    rol: str
    IdUsuario: Optional[int] = Field(default=None, foreign_key="usuario.IdUsuario")
    usuario: Optional["Usuario"] = Relationship(back_populates="perfiles")
    cursos: list["Curso"] = Relationship(back_populates="perfil")

class PerfilCreate(PerfilBase):
    Descripcion: str
    rol: str
    IdUsuario: int

class PerfilPublic(PerfilBase):
    IdPerfil: int
    Descripcion: str
    rol: str
    IdUsuario: int
    usuario: Optional["UsuarioPublic"] = None  

class PerfilUpdate(SQLModel):
    foto: Optional[str] = None
    Descripcion: Optional[str] = None

from models.usuarios import UsuarioPublic
PerfilPublic.model_rebuild()