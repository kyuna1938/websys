import uvicorn
from error import ConsistencyError, ResourceNotFoundError, UnauthorizedError
from fastapi import FastAPI, Request, status
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from starlette.middleware.cors import CORSMiddleware
from starlette.status import (HTTP_401_UNAUTHORIZED, HTTP_404_NOT_FOUND,
                              HTTP_500_INTERNAL_SERVER_ERROR)

from routers import rank

app = FastAPI()

app.include_router(rank.router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
    expose_headers=["content-disposition"],
)



@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    exc_str = f'{exc}'.replace('\n', ' ').replace('   ', ' ')
    print(f"{request}: {exc_str}")
    content = {'status_code': 10422, 'message': exc_str, 'data': None}
    return JSONResponse(
        status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
        content=content,
    )


@app.exception_handler(ResourceNotFoundError)
async def resource_not_found_exception_handler(request: Request, exc: ResourceNotFoundError):
    exc_str = f'{exc}'.replace('\n', ' ').replace('   ', ' ')
    content = {'status_code': 10404, 'message': exc_str, 'data': None}
    return JSONResponse(
        status_code=HTTP_404_NOT_FOUND,
        content=content
    )


@app.exception_handler(UnauthorizedError)
async def unauthorized_exception_handler(request: Request, exc: UnauthorizedError):
    exc_str = f'{exc}'.replace('\n', ' ').replace('   ', ' ')
    content = {'status_code': 10401, 'message': exc_str, 'data': None}
    return JSONResponse(
        status_code=HTTP_401_UNAUTHORIZED,
        content=content
    )


@app.exception_handler(ConsistencyError)
async def consistency_exception_handler(request: Request, exc: ConsistencyError):
    exc_str = f'{exc}'.replace('\n', ' ').replace('   ', ' ')
    content = {'status_code': 10500, 'message': exc_str, 'data': None}
    return JSONResponse(
        status_code=HTTP_500_INTERNAL_SERVER_ERROR,
        content=content
    )

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=4000)

