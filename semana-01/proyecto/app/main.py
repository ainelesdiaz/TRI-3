from fastapi import FastAPI
from app.routers import users, tasks, categories, stats

app = FastAPI(
    title="Sistema de Gestión de Tareas",
    version="1.0.0",
    description="API para gestionar usuarios, tareas y categorías"
)

app.include_router(users.router, prefix="/users", tags=["Users"])
app.include_router(tasks.router, prefix="/tasks", tags=["Tasks"])
app.include_router(categories.router, prefix="/categories", tags=["Categories"])
app.include_router(stats.router, prefix="/stats", tags=["Statistics"])

@app.get("/")
def root():
    return {"message": "API de Gestión de Tareas lista 🚀"}
