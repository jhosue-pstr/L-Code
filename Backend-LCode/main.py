from fastapi import FastAPI
from config.database import create_db_and_tables
from routers.users import router as users_router
from routers.perfiles import router as perfiles_router
from routers.cursos import router as cursos_router
from routers.inscripciones import router as inscripciones_router
app = FastAPI()

app.include_router(users_router, prefix="/api", tags=["users"])
app.include_router(perfiles_router, prefix="/api", tags=["perfiles"])
app.include_router(cursos_router, prefix="/api", tags=["cursos"])
app.include_router(inscripciones_router, prefix="/api", tags=["inscripciones"])

@app.on_event("startup")
def on_startup():
    create_db_and_tables()

@app.get("/")
def read_root():
    return {"message": "API funcionando"}