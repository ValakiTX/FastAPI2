from fastapi import FastAPI

from routes import users, items


app = FastAPI()

# Include routers
app.include_router(users.router, prefix="/users", tags=["Users"])
app.include_router(items.router, prefix="/items", tags=["Items"])


@app.get("/")
def root():
    """Return a welcome message."""
    return {"message": "Welcome to the FastAPI application!"}
