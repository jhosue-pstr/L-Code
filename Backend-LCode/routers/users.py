from fastapi import APIRouter
from controlers.Usuario import *

user = APIRouter()

@user.get("/api/usuarios/")
def ObtenerUsuario():
    LeerUsuario()
    return {"message": "Lista de usuarios"}


@user.post("/api/usuarios/")
def AgregarUsuario(usuario: Usuario):
    CrearUsuario()
    return {"message": "Usuario creado"}