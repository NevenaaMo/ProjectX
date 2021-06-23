"""Main file, declares app, middleware, registers routers and starts the uvicorn server.
"""
from fastapi import FastAPI, Depends
from fastapi.responses import RedirectResponse
import uvicorn
import os
from fastapi.middleware.cors import CORSMiddleware
from routers import countries, categories, shops, users, oauth2
from fastapi.security import OAuth2PasswordBearer


app = FastAPI(
    title="ProjectStorm",
    description="The API for the new no name project, built with Fast API.",
    version="1.0"
)
origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

@app.get('/')
def index():
    response = RedirectResponse("/docs")
    return response

@app.get("/items/")
async def read_items(token: str = Depends(oauth2_scheme)):
    return {"token": token}

app.include_router(users.router)
app.include_router(countries.router)
app.include_router(categories.router)
app.include_router(oauth2.router)
app.include_router(shops.router)


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=os.environ.get("PORT", 5000))
