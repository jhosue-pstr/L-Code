from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session
from config.database import get_session
from models.curso import CursoCreate, CursoPublic, CursoUpdate
from controlers.Curso import (
    LeerCursos, CrearCurso, LeerCursoPorId, ActualizarCurso, EliminarCurso
)

router = APIRouter()
@router.get("/cursos/", response_model=list[CursoPublic])
def ObtenerCursos(
    session: Session = Depends(get_session),
    offset: int = 0,
    limit: int = 100,
):
    return LeerCursos(session, offset=offset, limit=limit)  

@router.post("/cursos/", response_model=CursoPublic)
def Agregar_Curso(curso: CursoCreate, session: Session = Depends(get_session)):
    return CrearCurso(curso, session)

@router.get("/cursos/{IdCurso}", response_model=CursoPublic)  
def Obtener_Curso_Por_Id(IdCurso: int, session: Session = Depends(get_session)):
    return LeerCursoPorId(IdCurso, session)

@router.patch("/cursos/{IdCurso}", response_model=CursoPublic)
def Actualizar_Curso(IdCurso: int, datos: CursoUpdate, session: Session = Depends(get_session)):
    return ActualizarCurso(IdCurso, datos, session)

@router.delete("/cursos/{IdCurso}")
def Eliminar_Curso(IdCurso: int, session: Session = Depends(get_session)):
    return EliminarCurso(IdCurso, session)

