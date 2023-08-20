from fastapi import FastAPI, Depends
from app.endpoints import phrases, sections


def create_server():
    server = FastAPI(debug=True)
    server.include_router(phrases.router)
    server.include_router(sections.router)
    return server

app = create_server()
