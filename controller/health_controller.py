from fastapi import APIRouter
from fastapi.responses import JSONResponse
import logging

router = APIRouter()
@router.get("/health", tags=["Health"])

async def health_check():
    """
    Health check endpoint to verify the service is running.
    """
    try:
        logging.info("Health check endpoint called")
        return JSONResponse(
            status_code=200,
            content={"status": "healthy", 
                     "message": "Service is running nomally"
            },
        )
    except Exception as e:
        logging.error(f"Health check failed: {str(e)}")
        return JSONResponse(
            status_code=503,
            content={
                "status": "unhealthy", 
                "message": f"Service is not running properly: {str(e)}"
                },
        )