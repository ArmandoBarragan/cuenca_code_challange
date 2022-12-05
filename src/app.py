from fastapi import FastAPI


app = FastAPI()


@app.get("/solutions/")
def get_solutions():
    return "solutions"