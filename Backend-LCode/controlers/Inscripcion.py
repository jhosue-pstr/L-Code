from typing import Annotated
from fastapi import Depends, HTTPException, Query
from sqlmodel import Session, select
from config.database import get_session
from models.inscripcion import Inscripcion, InscripcionCreate, InscripcionPublic, InscripcionUpdate
from models.usuarios import Usuario, UsuarioPublic
from models.curso import Curso, CursoPublic


SessionDep = Annotated[Session, Depends(get_session)]

def CrearInscripcion(inscripcion:InscripcionCreate,session : Session)-> InscripcionPublic:
    nueva_inscripcion = Inscripcion.model_validate(inscripcion)
    session.add(nueva_inscripcion)
    session.commit()
    session.refresh(nueva_inscripcion)
    return InscripcionPublic.model_validate(nueva_inscripcion)



def LeerInscripciones(session:Session,offset:int = 0 , limit:Annotated[int,Query(le=100)]=100)-> list[InscripcionPublic]:
    inscripciones = session.exec(select(Inscripcion).offset(offset).limit(limit)).all()

    resultados = []
    for inscripcion in inscripciones:
        inscripcion_public = InscripcionPublic.model_validate(inscripcion)

        if inscripcion.IdCurso:
            curso = session.get(Curso,inscripcion.IdCurso)
            if curso:
                inscripcion_public.curso = CursoPublic.model_validate(curso)

        if inscripcion.IdUsuario:
            usuario = session.get(Usuario,inscripcion.IdUsuario)
            if usuario:
                inscripcion_public.usuario = UsuarioPublic.model_validate(usuario)

        resultados.append(inscripcion_public)
    return resultados


def LeerInscripcionPorId(IdInscripcion:int,session:Session)-> InscripcionPublic:
    inscripcion = session.get(Inscripcion,IdInscripcion)
    if not inscripcion:
        raise HTTPException(status_code=404,detail="Inscripcion no encontrada")
    
    inscripcion_public = InscripcionPublic.model_validate(inscripcion)

    if inscripcion.IdCurso:
        curso = session.get(Curso,inscripcion.IdCurso)
        if curso:
            inscripcion_public.curso = CursoPublic.model_validate(curso)

    if inscripcion.IdUsuario:
        usuario = session.get(Usuario,inscripcion.IdUsuario)
        if usuario:
            inscripcion_public.usuario = UsuarioPublic.model_validate(usuario)

    return inscripcion_public

def ActualizarInscripcion(IdInscripcion:int,datos:InscripcionUpdate,session:Session)-> InscripcionPublic:
    inscripcion_db = session.get(Inscripcion,IdInscripcion)
    if not inscripcion_db:
        raise HTTPException(status_code=404,detail="Inscripcion no encontrada")
    
    update_data = datos.model_dump(exclude_unset=True)
    inscripcion_db.sqlmodel_update(update_data)

    session.add(inscripcion_db)
    session.commit()
    session.refresh(inscripcion_db)

    inscripcion_public = InscripcionPublic.model_validate(inscripcion_db)

    if inscripcion_db.IdCurso:
        curso = session.get(Curso,inscripcion_db.IdCurso)
        if curso:
            inscripcion_public.curso = CursoPublic.model_validate(curso)

    if inscripcion_db.IdUsuario:
        usuario = session.get(Usuario,inscripcion_db.IdUsuario)
        if usuario:
            inscripcion_public.usuario = UsuarioPublic.model_validate(usuario)

    return inscripcion_public


def EliminarInscripcion(IdInscripcion:int,session:Session):
    inscripcion = session.get(Inscripcion,IdInscripcion)
    if not inscripcion:
        raise HTTPException(status_code=404,detail="Inscripcion no encontrada")
    session.delete(inscripcion)
    session.commit()
    return {"message":"Inscripcion eliminada"}

