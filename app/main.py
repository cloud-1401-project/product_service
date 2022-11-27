from config import engine
from config import metadata
from config import app
from typing import Union
import uvicorn
from fastapi import Request, Header
from fastapi.responses import JSONResponse
#from core.route import products_route
from core.auth import has_access

# app.include_router(products_route, prefix="/api/products", tags=["products"])


@app.middleware("http")
async def add_process_time_header(request: Request, call_next):
    token = request.headers.get('authorization')
    if token is None or has_access(request.method, request.url.path, token) == False:
        return JSONResponse(status_code=401,
                            content={"message": "You don't have access to this resource."})
    response = await call_next(request)
    return response

if __name__ == '__main__':
    metadata.create_all(engine)
    uvicorn.run("main:app", host="127.0.0.1", port=8000)
