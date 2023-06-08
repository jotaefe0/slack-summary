from fastapi import FastAPI, Response, BackgroundTasks
import utils
import params

app = FastAPI()


def send_summary():
    summary = utils.create_summary()
    utils.send_msg(params.CHANNEL, summary)

@app.post("/summary")
async def trigger_endpoint(background_tasks: BackgroundTasks):
    background_tasks.add_task(send_summary)
    return Response(status_code=200)