from api.models.auth.accounts import LoginModel, RegistrationRequest
from api.services.auth_service import RegistrationService, get_registration_service
from fastapi import APIRouter, Depends, status

router = APIRouter(prefix="/auth", tags=["auth"])

@router.post("/register", status_code=status.HTTP_201_CREATED)
async def register(request: RegistrationRequest, service: RegistrationService = Depends(get_registration_service)):  # noqa: B008
    await service.register_user(request)
    return {"message": "User registered successfully."}

@router.post("/login")
async def login(request: LoginModel):
    return {"message": "Login endpoint"}
