from sqlmodel import Field, SQLModel, Relationship
from typing import Optional
import datetime


class ContenidoBase(SQLModel):
    Titulo: str
    Descripcion: str
    Tipo: str
    recurso: str
    duracion: float
    orden: int


class Contenido(ContenidoBase, table=True):
    IdContenido: Optional[int] = Field(default=None, primary_key=True)
    FechaCreacion: datetime.date = Field(default_factory=datetime.datetime.utcnow)
    estado: bool = True
    IdCurso: Optional[int] = Field(default=None, foreign_key="curso.IdCurso")
    curso: Optional["Curso"] = Relationship(back_populates="contenidos")


class ContenidoCreate(ContenidoBase):
    IdCurso: int 


class ContenidoPublic(ContenidoBase):
    IdContenido: int
    FechaCreacion: datetime.date
    estado: bool
    IdCurso: int


class ContenidoUpdate(SQLModel):
    Titulo: Optional[str] = None
    Descripcion: Optional[str] = None
    Tipo: Optional[str] = None
    recurso: Optional[str] = None
    duracion: Optional[float] = None
    orden: Optional[int] = None
    estado: Optional[bool] = None