from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app import routes

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(routes.router)

@app.get("/api/health")
def health_check():
    return {"status": "GeoRiskAI backend OK!"}


@app.get("/")
def root():
    return {"message": "Welcome to GeoRiskAI backend!"}
