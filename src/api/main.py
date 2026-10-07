from collections.abc import AsyncIterator
from contextlib import asynccontextmanager

from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine

from api.db_configuration import get_database_settings
from api.routers import auth
from api.services.auth_service import InvalidPasswordError


@asynccontextmanager
async def lifespan(app: FastAPI):
    settings = get_database_settings()
    engine = create_async_engine(settings.url, pool_pre_ping=True)
    app.state.session_factory = async_sessionmaker(engine, expire_on_commit=False)
    yield
    await engine.dispose()

app = FastAPI(lifespan=lifespan)
app.include_router(auth.router)

@app.exception_handler(InvalidPasswordError)
async def invalid_password_exception_handler(request, exc: InvalidPasswordError):
    return JSONResponse(
        status_code=400,
        content={"message": str(exc)},
    )

async def get_session(request: Request) -> AsyncIterator[AsyncSession]:
    async with request.app.state.session_factory() as session:
        yield session