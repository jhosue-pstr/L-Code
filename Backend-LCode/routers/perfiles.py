from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session
from config.database import get_session
from models.perfil import PerfilCreate, PerfilPublic, PerfilUpdate
from controlers.Perfil import (
    LeerPerfiles, CrearPerfil, LeerPerfilPorId, ActualizarPerfil, EliminarPerfil  # ← CORREGIDO
)

router = APIRouter()
@router.get("/perfiles/", response_model=list[PerfilPublic])
def ObtenerPerfiles(
    session: Session = Depends(get_session),
    offset: int = 0,
    limit: int = 100,
):
    return LeerPerfiles(session, offset=offset, limit=limit)

@router.post("/perfiles/", response_model=PerfilPublic)
def Agregar_Perfil(perfil: PerfilCreate, session: Session = Depends(get_session)):
    return CrearPerfil(perfil, session)

@router.get("/perfiles/{IdPerfil}", response_model=PerfilPublic)
def Obtener_Perfil_Por_Id(IdPerfil: int, session: Session = Depends(get_session)):
    return LeerPerfilPorId(IdPerfil, session)   

@router.patch("/perfiles/{IdPerfil}", response_model=PerfilPublic)
def Actualizar_Perfil(IdPerfil: int, datos: PerfilUpdate, session: Session = Depends(get_session)):
    return ActualizarPerfil(IdPerfil, datos, session)  # ← CORREGIDO

@router.delete("/perfiles/{IdPerfil}")
def Eliminar_Perfil(IdPerfil: int, session: Session = Depends(get_session)):
    return EliminarPerfil(IdPerfil, session)