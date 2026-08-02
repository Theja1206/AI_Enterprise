from fastapi.responses import JSONResponse
from fastapi import Request
from app.core.exceptions import *

async def user_exists_handler(
        requests: Request,
        exc: UserAlreadyExistsException
):
    return JSONResponse(
        status_code=400,
        content={
            "Error":exc.message
        }
    )

async def user_not_found_handler(
        requests: Request,
        exc: UserNotFoundException
):
    return JSONResponse(
        status_code=404,
        content={
            "Error":exc.message
        }
    )

async def database_handler(
        requests: Request,
        exc: DatabaseException
):
    return JSONResponse(
        status_code=500,
        content={
            "Error":exc.message
        }
    )