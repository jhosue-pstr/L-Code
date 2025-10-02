from typing import Annotated
from fastapi import Depends, HTTPException, Query
from sqlmodel import Session, select
from config.database import get_session
from models.perfil import Perfil, PerfilCreate, PerfilPublic, PerfilUpdate
from models.usuarios import Usuario, UsuarioPublic  # ← Importar Usuario y UsuarioPublic

SessionDep = Annotated[Session, Depends(get_session)]

def CrearPerfil(perfil: PerfilCreate, session: Session) -> PerfilPublic:
    nuevo_perfil = Perfil.model_validate(perfil)
    session.add(nuevo_perfil)
    session.commit()
    session.refresh(nuevo_perfil)
    return PerfilPublic.model_validate(nuevo_perfil)

def LeerPerfiles(session: Session, offset: int = 0, limit: Annotated[int, Query(le=100)] = 100) -> list[PerfilPublic]:
    perfiles = session.exec(select(Perfil).offset(offset).limit(limit)).all()
    
    resultados = []
    for perfil in perfiles:
        perfil_public = PerfilPublic.model_validate(perfil)
        
        if perfil.IdUsuario:
            usuario = session.get(Usuario, perfil.IdUsuario)
            if usuario:
                perfil_public.usuario = UsuarioPublic.model_validate(usuario)
        
        resultados.append(perfil_public)
    
    return resultados

def LeerPerfilPorId(IdPerfil: int, session: Session) -> PerfilPublic:
    perfil = session.get(Perfil, IdPerfil)
    if not perfil:
        raise HTTPException(status_code=404, detail="Perfil no encontrado")
    
    perfil_public = PerfilPublic.model_validate(perfil)
    
    if perfil.IdUsuario:
        usuario = session.get(Usuario, perfil.IdUsuario)
        if usuario:
            perfil_public.usuario = UsuarioPublic.model_validate(usuario)
    
    return perfil_public

def ActualizarPerfil(IdPerfil: int, datos: PerfilUpdate, session: Session) -> PerfilPublic:
    perfil_db = session.get(Perfil, IdPerfil)
    if not perfil_db:
        raise HTTPException(status_code=404, detail="Perfil no encontrado")
    
    update_data = datos.model_dump(exclude_unset=True)
    perfil_db.sqlmodel_update(update_data)

    session.add(perfil_db)
    session.commit()
    session.refresh(perfil_db)
    
    perfil_public = PerfilPublic.model_validate(perfil_db)
    
    if perfil_db.IdUsuario:
        usuario = session.get(Usuario, perfil_db.IdUsuario)
        if usuario:
            perfil_public.usuario = UsuarioPublic.model_validate(usuario)
    
    return perfil_public

def EliminarPerfil(IdPerfil: int, session: Session):
    perfil = session.get(Perfil, IdPerfil)
    if not perfil:
        raise HTTPException(status_code=404, detail="Perfil no encontrado")
    session.delete(perfil)
    session.commit()
    return {"message": "Perfil eliminado"}