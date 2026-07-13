from fastapi import FastAPI


app = FastAPI()


@app.get("/")
def home():
    return {
        "message": "Hello Developer Roadmap"
    }


@app.get("/user/{name}")
def user(name:str):
    return {
        "user": name
    }
