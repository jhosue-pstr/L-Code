from fastapi import APIRouter, Depends
from sqlmodel import Session
from config.database import get_session
from models.usuarios import UsuarioCreate, UsuarioPublic, UsuarioUpdate
from controlers.Usuario import (
    LeerUsuarios, CrearUsuario, LeerUsuarioPorId, ActualizarUsuario, EliminarUsuario
)

user = APIRouter()


@user.get("/api/usuarios/", response_model=list[UsuarioPublic])
def ObtenerUsuario(
    session: Session = Depends(get_session),
    offset: int = 0,
    limit: int = 100,
):
    return LeerUsuarios(session, offset=offset, limit=limit)


@user.post("/api/usuarios/", response_model=UsuarioPublic)
def Agregar_Usuario(usuario: UsuarioCreate, session: Session = Depends(get_session)):
    return CrearUsuario(usuario, session)


@user.get("/api/usuarios/{IdUsuario}", response_model=UsuarioPublic)
def Obtener_Usuario_Por_Id(IdUsuario: int, session: Session = Depends(get_session)):
    return LeerUsuarioPorId(IdUsuario, session)


@user.patch("/api/usuarios/{IdUsuario}", response_model=UsuarioPublic)
def Actualizar_Usuario(IdUsuario: int, datos: UsuarioUpdate, session: Session = Depends(get_session)):
    return ActualizarUsuario(IdUsuario, datos, session)


@user.delete("/api/usuarios/{IdUsuario}")
def Eliminar_Usuario(IdUsuario: int, session: Session = Depends(get_session)):
    return EliminarUsuario(IdUsuario, session)
