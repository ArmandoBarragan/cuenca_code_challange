import uvicorn
from src.settings.settings import SERVER


if __name__ == "__main__":
    """ I was not going to make a server, but I did not take into account that the container would constantly
    restart, so this was easier in the end. Plus, this way you can check with swaggerUI easily."""
    uvicorn.run("src.app:app",
                host=SERVER["HOST"],
                port=SERVER["PORT"],
                reload=SERVER["DEBUG"])