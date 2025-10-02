from typing import Annotated
from fastapi import Depends, HTTPException, Query
from sqlmodel import Session, select
from config.database import *
from models.perfil import *

SessionDep = Annotated[Session, Depends(get_session)]

