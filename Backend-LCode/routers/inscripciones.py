from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session
from config.database import get_session
from models.inscripcion import InscripcionCreate, InscripcionPublic, InscripcionUpdate
from controlers.Inscripcion import (
    LeerInscripciones, CrearInscripcion, LeerInscripcionPorId, ActualizarInscripcion, EliminarInscripcion
)


router = APIRouter()

@router.get("/inscripciones/", response_model=list[InscripcionPublic])
def ObtenerInscripciones(
    session: Session = Depends(get_session),
    offset: int = 0,
    limit: int = 100,
):
    return LeerInscripciones(session, offset=offset, limit=limit)

@router.post("/inscripciones/", response_model=InscripcionPublic)
def Agregar_Inscripcion(inscripcion: InscripcionCreate, session: Session = Depends(get_session)):
    return CrearInscripcion(inscripcion, session)

@router.get("/inscripciones/{IdInscripcion}", response_model=InscripcionPublic)
def Obtener_Inscripcion_Por_Id(IdInscripcion: int, session: Session = Depends(get_session)):
    return LeerInscripcionPorId(IdInscripcion, session)

@router.patch("/inscripciones/{IdInscripcion}", response_model=InscripcionPublic)
def Actualizar_Inscripcion(IdInscripcion: int, datos: InscripcionUpdate, session: Session = Depends(get_session)):
    return ActualizarInscripcion(IdInscripcion, datos, session)


@router.delete("/inscripciones/{IdInscripcion}")
def Eliminar_Inscripcion(IdInscripcion: int, session: Session = Depends(get_session)):
    return EliminarInscripcion(IdInscripcion, session)  