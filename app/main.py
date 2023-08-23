from fastapi import FastAPI
from app.endpoints import phrases, sections
from fastapi.middleware.cors import CORSMiddleware
from app.security.auth import AuthorizeRequestMiddleware


def create_server():
    server = FastAPI(debug=True)
    server.add_middleware(AuthorizeRequestMiddleware)
    server.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    server.include_router(phrases.router)
    server.include_router(sections.router)

    return server


app = create_server()
