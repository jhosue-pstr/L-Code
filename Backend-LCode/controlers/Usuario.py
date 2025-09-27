from typing import Annotated
from fastapi import Depends, HTTPException, Query
from sqlmodel import Session, select
from config.database import get_session
from models.usuarios import Usuario
import datetime



SessionDep = Annotated[Session, Depends(get_session)]

def CrearUsuario(usuario: Usuario, session: SessionDep) -> Usuario:
    nuevo_usuario = Usuario(
        Nombre=usuario.Nombre,
        Apellido=usuario.Apellido,
        Correo=usuario.Correo,
        Contrasena=usuario.Contrasena,
        FechaRegistro=str(datetime.datetime.now()),
        estado=True
    )
    session.add(nuevo_usuario)
    session.commit()
    session.refresh(nuevo_usuario)
    return nuevo_usuario


def LeerUsuario(session: SessionDep,
    offset: int = 0,
    limit: Annotated[int, Query(le=100)] = 100,
) -> list[Usuario]:
    usuarios = session.exec(select(Usuario).offset(offset).limit(limit)).all()
    return usuarios


