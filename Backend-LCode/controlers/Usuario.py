from typing import Annotated
from fastapi import Depends, HTTPException, Query
from sqlmodel import Session, select
from config.database import get_session
from models.usuarios import Usuario, UsuarioCreate, UsuarioPublic, UsuarioUpdate
import datetime

SessionDep = Annotated[Session, Depends(get_session)]

def CrearUsuario(usuario: UsuarioCreate, session: Session) -> UsuarioPublic:
    nuevo_usuario = Usuario.model_validate(usuario)
    nuevo_usuario.estado = True
    
    session.add(nuevo_usuario)
    session.commit()
    session.refresh(nuevo_usuario)
    return UsuarioPublic.model_validate(nuevo_usuario)

def LeerUsuarios(
    session: Session,
    offset: int = 0,
    limit: Annotated[int, Query(le=100)] = 100,
) -> list[UsuarioPublic]:
    usuarios = session.exec(select(Usuario).offset(offset).limit(limit)).all()
    return [UsuarioPublic.model_validate(u) for u in usuarios]

def LeerUsuarioPorId(IdUsuario: int, session: Session) -> UsuarioPublic:
    usuario = session.get(Usuario, IdUsuario)
    if not usuario:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    return UsuarioPublic.model_validate(usuario)

def ActualizarUsuario(IdUsuario: int, datos: UsuarioUpdate, session: Session) -> UsuarioPublic:
    usuario_db = session.get(Usuario, IdUsuario)
    if not usuario_db:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    
    update_data = datos.model_dump(exclude_unset=True)
    usuario_db.sqlmodel_update(update_data)

    session.add(usuario_db)
    session.commit()
    session.refresh(usuario_db)
    return UsuarioPublic.model_validate(usuario_db)

def EliminarUsuario(IdUsuario: int, session: Session):
    usuario = session.get(Usuario, IdUsuario)
    if not usuario:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    session.delete(usuario)
    session.commit()
    return {"message": "Usuario eliminado"}
