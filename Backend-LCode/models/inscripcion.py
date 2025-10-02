from sqlmodel import Field, SQLModel, Relationship
from typing import Optional
import datetime


class InscripcionBase(SQLModel):
    Progreso: Optional[float] = 0.0


class Inscripcion(InscripcionBase, table=True):
    IdInscripcion: Optional[int] = Field(default=None, primary_key=True)
    FechaInscripcion: datetime.date = Field(default_factory=datetime.datetime.utcnow)
    estado: bool = True
    IdCurso: Optional[int] = Field(default=None, foreign_key="curso.IdCurso")
    IdUsuario: Optional[int] = Field(default=None, foreign_key="usuario.IdUsuario")
    
    curso: Optional["Curso"] = Relationship(back_populates="inscripciones")
    usuario: Optional["Usuario"] = Relationship(back_populates="inscripciones")


class InscripcionCreate(InscripcionBase):
    IdCurso: int 
    IdUsuario: int 


class InscripcionPublic(InscripcionBase):
    IdInscripcion: int
    FechaInscripcion: datetime.date
    estado: bool
    IdCurso: int
    curso : Optional["CursoPublic"] = None
    IdUsuario: int
    usuario: Optional["UsuarioPublic"] = None


class InscripcionUpdate(SQLModel):
    Progreso: Optional[float] = None
    estado: Optional[bool] = None

from models.curso import CursoPublic
from models.usuarios import UsuarioPublic
InscripcionPublic.model_rebuild()    