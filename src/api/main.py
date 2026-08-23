from contextlib import asynccontextmanager

from fastapi import FastAPI

from api.routers import auth


@asynccontextmanager
async def lifespan(app: FastAPI):
    yield

app = FastAPI(lifespan=lifespan)
app.include_router(auth.router)