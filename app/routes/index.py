from datetime import datetime, datetimr

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from starlette.responses import Response

from app.database.conn import db
from app.database.schema import Users

router = APIRouter()


@router.get("/")
async def index(session: Session = Depends(db.session)):
    """
    ELB health check API
    :return:
    """
    
    Users.create(session,auto_commit=True, name="")
    current_time = datetime.utcnow()
    return Response(f"Notification API (UTC: {current_time.strftime('%Y.%m.%d %H:%M:%S')})")