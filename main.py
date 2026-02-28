from fastapi import FastAPI


app = FastAPI()


@app.get("/")
async def main():
    return {"message":"Hello World!"}


@app.get("/greet/{name}")
async def greet(name:str):
    return {"message":f"hello {name}"}


@app.get("/greet/{name}")
async def greet(name:str):
    return {"message":f"hello {name}"}    

