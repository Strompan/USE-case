from fastapi import FastAPI
from Aviaries.routers import router

app = FastAPI()
app.include_router(router)
