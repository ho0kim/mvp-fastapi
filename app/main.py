import uvicorn
from fastapi import FastAPI

from app.common.config import conf


def create_app():
    """
    APP START
    """
    app = FastAPI()
    
    #미들웨어 정의
    #라우트 정의
    #DB 정의
    
    return app

app = create_app()

if __name__ == "__maiun__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=conf().PROJ_RELOAD)
