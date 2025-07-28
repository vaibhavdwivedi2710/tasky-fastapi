from fastapi import Request, Response
from fastapi.responses import JSONResponse
import logging
from uuid import uuid4

from app_secrets import TASKY_SECRET_KEY

from fastapi import Request, Response
from fastapi.responses import JSONResponse
import logging

# Middleware to check authentication for incoming requests
async def check_authentication(request: Request, call_next) -> Response:
    """
    Middleware to check authentication for incoming requests.
    """
    if request.url.path.startswith("/health"):
        return await call_next(request)

    client_secret = request.headers.get("x-client-secret")
    if not client_secret:
        logging.warning(f"Authorization attempt failed: Missing Client Secret Header")
        return JSONResponse(
            status_code=401,
            content={"message": "Unauthorized:Client Secret header is required"},
        )
    if client_secret != TASKY_SECRET_KEY:
        logging.warning(f"Authorization attempt failed: Invalid Client Secret Header")
        return JSONResponse(
            status_code=403,
            content={"message": "Forbidden:Invalid Client-Secret header provided"},
        )
    logging.debug("Authorization successful")
    return await call_next(request)


# Middleware to add a trace ID to the response headers
async def add_trace_id(request: Request, call_next):
    trace_id= str(uuid4())
    response = await call_next(request)
    response.headers["X-Trace-ID"] = trace_id
    return response