from fastapi import FastAPI
from routes.study_route import router as study_routes

app = FastAPI()

app.include_router(study_routes)

# main page
@app.get("/")
def read_root():
    return {"Hello": "World"}

# testing pending !