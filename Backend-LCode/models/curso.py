from sqlmodel import Field, SQLModel, Relationship
from typing import Optional
import datetime


class CursoBase(SQLModel):
    Titulo: str
    Descripcion: str
    Duracion: int 
    Nivel: str


class Curso(CursoBase, table=True):
    IdCurso: Optional[int] = Field(default=None, primary_key=True)
    FechaCreacion: datetime.date = Field(default_factory=datetime.datetime.utcnow)
    estado: bool = True
    IdPerfil: Optional[int] = Field(default=None, foreign_key="perfil.IdPerfil")
    perfil: Optional["Perfil"] = Relationship(back_populates="cursos")
    inscripciones: list["Inscripcion"] = Relationship(back_populates="curso")
    contenidos: list["Contenido"] = Relationship(back_populates="curso")


class CursoCreate(CursoBase):
    IdPerfil: int  


class CursoPublic(CursoBase):
    IdCurso: int
    FechaCreacion: datetime.date
    estado: bool
    IdPerfil: int
    perfil: Optional["PerfilPublic"] = None  



class CursoUpdate(SQLModel):
    Titulo: Optional[str] = None
    Descripcion: Optional[str] = None
    Duracion: Optional[int] = None
    Nivel: Optional[str] = None
    estado: Optional[bool] = None
    IdPerfil: Optional[int] = None


from models.perfil import PerfilPublic
CursoPublic.model_rebuild()  