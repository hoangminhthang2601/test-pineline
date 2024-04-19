"""
Define all the API.
"""

from fastapi import FastAPI, Response, status

# from .api import api_router

descriptions = """
Welcome to AILIVER API documentation!
Here you will able to discover all of the ways you can interact with the AILIVER API.
"""

app = FastAPI(
    title="AILIVER delivery services",
    description=descriptions,
    docs_url="/api/docs",
    redoc_url="/api/schemas",
)

# app.include_router(api_router)


@app.get("/health-check", tags=["Health Check,"])
def health_check():
    return Response(status_code=status.HTTP_200_OK, content="OK")
