from fastapi import FastAPI
from .database import engine, Base
from .routes import tasks,users

Base.metadata.create_all(bind=engine)

app = FastAPI()
app = FastAPI()

app.include_router(tasks.router)
app.include_router(users.router)

# IMPORTANT LINE
app.include_router(tasks.router)

@app.get("/")
def read_root():
    return {"message": "Task Manager API running"}