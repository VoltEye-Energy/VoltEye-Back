from fastapi import FastAPI

from src.controllers import health_controller, medicao_controller


app = FastAPI(
    title="VoltEye API",
    description="API para receber medicoes de consumo eletrico enviadas por dispositivos IoT.",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc",
)

app.include_router(health_controller.router)
app.include_router(medicao_controller.router)
