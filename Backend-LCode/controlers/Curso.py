from typing import Annotated
from fastapi import Depends, HTTPException, Query
from sqlmodel import Session, select
from config.database import get_session
from models.curso import Curso, CursoCreate, CursoPublic, CursoUpdate
from models.perfil import Perfil, PerfilPublic 

SessionDep = Annotated[Session, Depends(get_session)]

def CrearCurso(curso: CursoCreate, session: Session) -> CursoPublic:
    nuevo_curso = Curso.model_validate(curso)
    session.add(nuevo_curso)
    session.commit()
    session.refresh(nuevo_curso)
    return CursoPublic.model_validate(nuevo_curso)

def LeerCursos(session: Session, offset: int = 0, limit: Annotated[int, Query(le=100)] = 100) -> list[CursoPublic]:
    cursos = session.exec(select(Curso).offset(offset).limit(limit)).all()

    resultados = []
    for curso in cursos:
        curso_public = CursoPublic.model_validate(curso)
        if curso.IdPerfil:
            perfil = session.get(Perfil, curso.IdPerfil)
            if perfil: 
                curso_public.perfil = PerfilPublic.model_validate(perfil)
        resultados.append(curso_public)

    return resultados        

def LeerCursoPorId(IdCurso: int, session: Session) -> CursoPublic:
    curso = session.get(Curso, IdCurso)
    if not curso:
        raise HTTPException(status_code=404, detail="Curso no encontrado")
    
    curso_public = CursoPublic.model_validate(curso)

    if curso.IdPerfil:
        perfil = session.get(Perfil, curso.IdPerfil)
        if perfil:
            curso_public.perfil = PerfilPublic.model_validate(perfil)

    return curso_public

def ActualizarCurso(IdCurso: int, datos: CursoUpdate, session: Session) -> CursoPublic:
    curso_db = session.get(Curso, IdCurso)
    if not curso_db:
        raise HTTPException(status_code=404, detail="Curso no encontrado")
    
    update_data = datos.model_dump(exclude_unset=True)
    curso_db.sqlmodel_update(update_data)

    session.add(curso_db)
    session.commit()
    session.refresh(curso_db)
    
    curso_public = CursoPublic.model_validate(curso_db)

    if curso_db.IdPerfil:
        perfil = session.get(Perfil, curso_db.IdPerfil)
        if perfil:
            curso_public.perfil = PerfilPublic.model_validate(perfil)

    return curso_public

def EliminarCurso(IdCurso: int, session: Session):
    curso = session.get(Curso, IdCurso)
    if not curso:
        raise HTTPException(status_code=404, detail="Curso no encontrado")
    session.delete(curso)
    session.commit()
    return {"message": "Curso eliminado"}