from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "hi from Fastapi me checked deploy success git runner :/"}