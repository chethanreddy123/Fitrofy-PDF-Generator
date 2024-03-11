from fastapi import FastAPI
from routers import pdf_controller
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI(
    title="Fitrofy PDF API",
)

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(pdf_controller.router)
