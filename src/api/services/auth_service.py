from api.models.auth.accounts import RegistrationRequest
from zxcvbn import zxcvbn  # pyright: ignore[reportMissingModuleSource]


class InvalidPasswordError(Exception):
    ...

class RegistrationService:
    def __init__(self):
        ...

    async def register_user(self, registration_request: RegistrationRequest):
        unmasked_password = registration_request.password.get_secret_value()
        validation_result = zxcvbn(unmasked_password)

        if (validation_result["score"] < 3):
            raise InvalidPasswordError(
                "Password is too weak. Please choose a stronger password."
            )


def get_registration_service() -> RegistrationService:
    return RegistrationService()