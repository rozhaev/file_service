from fastapi import Body, FastAPI
from fastapi.responses import JSONResponse

from manager.task_manager import create_duplicate


app = FastAPI()


@app.post("/tasks", status_code=201)
def run_task(body=Body(...)):
    task = create_duplicate.delay(0)
    return JSONResponse({"task_id": task.id})

