from fastapi import FastAPI, HTTPException, Depends
from celery import Celery
import logging
import sys, os
# Adiciona o diretório pai ao sys.path
# sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
# print(sys.path)

from fastapi.encoders import jsonable_encoder
# from sqlalchemy.orm import Session
from pydantic import BaseModel
from typing import List

# from config.database import get_db, engine
# import models
# import schemas
# from models import user, post


# user.Base.metadata.create_all(bind=engine)
# post.Base.metadata.create_all(bind=engine)

class Schedule(BaseModel):
    x: int
    y: int

app = FastAPI()
simple_app = Celery('simple_worker', broker='redis://redis:6379/0', backend='redis://redis:6379/0')

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
stream_handler = logging.StreamHandler(sys.stdout)
log_formatter = logging.Formatter("%(asctime)s [%(processName)s: %(process)d] [%(threadName)s: %(thread)d] [%(levelname)s] %(name)s: %(message)s")
stream_handler.setFormatter(log_formatter)
logger.addHandler(stream_handler)

logger.info('API is starting up')

@app.get("/")
async def root():
    return {"message": "Welcome to my bookstore app!"}


@app.post("/new_schedule")
async def new_schedule(schedule: Schedule):
    logger.info("[FastAPI] Invoking Method ")    
    # queue name in task folder.function name
    r = simple_app.send_task('tasks.longtime_add', kwargs={'x': schedule.x, 'y': schedule.y})
    logger.info(f"[FastAPI] New task: {r.id}")
    return r.id


@app.get("/schedule_status/{task_id}")
async def schedule_status(task_id: str):
    status = simple_app.AsyncResult(task_id, app=simple_app)
    logger.info("[FastAPI] Status of the Task " + str(status.state))
    return "Status of the Task " + str(status.state)


@app.get("/schedule_result/{task_id}")
async def schedule_result(task_id: str):
    result = simple_app.AsyncResult(task_id).result
    return "Result of the Task: " + str(result)