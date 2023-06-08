from fastapi import FastAPI, Response, BackgroundTasks, Form
import utils
import params
from pydantic import BaseModel

app = FastAPI()

# class SlashCommandPayload(BaseModel):
#     channel_id: str
   

def send_summary(channel_id):
    summary = utils.create_summary(channel_id)
    utils.send_msg(channel_id, summary)

@app.post("/summary")
async def trigger_endpoint(background_tasks: BackgroundTasks, channel_id: str = Form(...)):
    #Slack backslash expects a response in a 3 sec so we process on background
    background_tasks.add_task(send_summary, channel_id)

    return Response(status_code=200)