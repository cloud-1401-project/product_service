from config import engine
from config import metadata
from config import app
import uvicorn
from fastapi import Request
from core.route import products_route

app.include_router(products_route, prefix="/api/products", tags=["products"])


# @app.middleware("http")
# async def add_process_time_header(request: Request, call_next):
#     x = getattr(request, 'is_authenticated', 'NOPE')
#     print(f'is auth {x}')
#     if hasattr(request, 'is_authenticated') and request.is_authenticated:
#         response = await call_next(request)
#         return response
#     token = request.headers.get('authorization')
#     print(f'token is {token}')
#     if token is None or has_access(request.method, request.url.path, token, request) == False:
#         return JSONResponse(status_code=401,
#                             content={"message": "You don't have access to this resource."})
#     response = await call_next(request)
#     return response

if __name__ == '__main__':
    metadata.create_all(engine)
    uvicorn.run("main:app", host="0.0.0.0", port=8000)
