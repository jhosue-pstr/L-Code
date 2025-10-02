from fastapi import APIRouter, Depends
from sqlmodel import Session
from config.database import get_session
from models.usuarios import UsuarioCreate, UsuarioPublic, UsuarioUpdate
from controlers.Usuario import (
    LeerUsuarios, CrearUsuario, LeerUsuarioPorId, ActualizarUsuario, EliminarUsuario
)

router = APIRouter()

@router.get("/usuarios/", response_model=list[UsuarioPublic])
def ObtenerUsuario(
    session: Session = Depends(get_session),
    offset: int = 0,
    limit: int = 100,
):
    return LeerUsuarios(session, offset=offset, limit=limit)

@router.post("/usuarios/", response_model=UsuarioPublic)
def Agregar_Usuario(usuario: UsuarioCreate, session: Session = Depends(get_session)):
    return CrearUsuario(usuario, session)

@router.get("/usuarios/{IdUsuario}", response_model=UsuarioPublic)
def Obtener_Usuario_Por_Id(IdUsuario: int, session: Session = Depends(get_session)):
    return LeerUsuarioPorId(IdUsuario, session)

@router.patch("/usuarios/{IdUsuario}", response_model=UsuarioPublic)
def Actualizar_Usuario(IdUsuario: int, datos: UsuarioUpdate, session: Session = Depends(get_session)):
    return ActualizarUsuario(IdUsuario, datos, session)

@router.delete("/usuarios/{IdUsuario}")
def Eliminar_Usuario(IdUsuario: int, session: Session = Depends(get_session)):
    return EliminarUsuario(IdUsuario, session)