from fastapi import FastAPI, Depends
from fastapi_crudrouter import SQLAlchemyCRUDRouter
from sqlalchemy.orm import Session
from app.database import get_db
from app.auth import register_user, login_user, refresh_token, get_my_info, get_current_user
from app.models import Post
from app.schemas import PostCreate, PostResponse

app = FastAPI()

# Auth Routes
app.post("/auth/register")(register_user)
app.post("/auth/login")(login_user)
app.post("/auth/refresh")(refresh_token)
app.get("/auth/me")(get_my_info)

# Post CRUD Router
post_router = SQLAlchemyCRUDRouter(
    schema=PostResponse,
    create_schema=PostCreate,
    db_model=Post,
    db=get_db,
    dependencies=[Depends(get_current_user)]
)
app.include_router(post_router, prefix="/posts", tags=["Posts"])
