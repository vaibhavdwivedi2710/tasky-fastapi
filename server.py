from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
import logging
import uvicorn
from uuid import uuid4

from middleware import check_authentication
from db.mongo_init import connect_to_mongo
#from routes.api_v1 import router  # assuming your router is defined in routes/api_v1.py

# Configure logging
logging.basicConfig(level=logging.INFO)
logging.info("--------Loaded environment variables ---------")
logging.info("----------Starting FastAPI Server ------------")

app = FastAPI(
    title="Taskfy FASTAPI",
    description="API for Taskfy application",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc",
    openapi_url="/openapi.json",
)

# MongoDB connection at startup
@app.on_event("startup")
async def startup_event():
    logging.info("--------------Starting MongoDB connection-----------------")
    connect_to_mongo()

# Middleware to validate x-request-id header
@app.middleware("http")
async def add_request_id(request: Request, call_next):
    if request.url.path.startswith("/health"):
        return await call_next(request)

    request_id = request.headers.get("x-request-id")
    if not request_id:
        return JSONResponse(
            status_code=401,
            content={"error": "Missing 'x-request-id' header"},
        )
    
    response = await call_next(request)
    return response

# Register authentication middleware
app.middleware("http")(check_authentication)

# Include API router
#app.include_router(router, prefix="/api/v1", tags=["v1"])

# Start the server
if __name__ == "__main__":
    uvicorn.run("server:app", host="0.0.0.0", port=8000, reload=True)