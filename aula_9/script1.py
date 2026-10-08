from fastapi import FastAPI

app = FastAPI()

@app.get("/saudacao")
def saudacao():
    return print("Olá")