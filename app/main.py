import uvicorn
from fastapi import FastAPI
from app.database.conn import db
from app.common.config import conf
from app.routes import index


def create_app():
    """
    APP START
    """
    c = conf()
    app = FastAPI()
    conf_dict = asdict(c)
    db.init_app(app, **conf_dict)
    
    #미들웨어 정의
    #라우트 정의
    #DB 정의
    
    app.include_router(index.router)
    return app

app = create_app()

if __name__ == "__maiun__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=conf().PROJ_RELOAD)
