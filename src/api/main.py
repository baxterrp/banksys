from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.responses import JSONResponse

from api.routers import auth
from api.services.auth_service import InvalidPasswordError


@asynccontextmanager
async def lifespan(app: FastAPI):
    yield

app = FastAPI(lifespan=lifespan)
app.include_router(auth.router)

@app.exception_handler(InvalidPasswordError)
async def invalid_password_exception_handler(request, exc: InvalidPasswordError):
    return JSONResponse(
        status_code=400,
        content={"message": str(exc)},
    )