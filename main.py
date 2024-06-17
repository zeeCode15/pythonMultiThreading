from fastapi import FastAPI, BackgroundTasks
from concurrent.futures import ThreadPoolExecutor
import myModule
import time

app = FastAPI()
executer = ThreadPoolExecutor(max_workers=10)

def myFunctionModule(inputVal: int):
    print(f"Task Started for input value: {inputVal}")
    return myModule.myFunctionModule(inputVal)


def background_task(future):
    result = future.result()
    print("The Task Completed Sucessfully !!")


@app.get("/")
def welcome():
    return "Welcome to Back-End"

@app.get("/task/")
def getTaskDone(inputVal: int, background_tasks: BackgroundTasks):

    future = executer.submit(myFunctionModule, inputVal)

    background_tasks.add_task(background_task, future)

    return {"inputValue": inputVal}
