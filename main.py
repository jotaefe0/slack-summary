from fastapi import FastAPI, Response, BackgroundTasks
import utils
import params
from pydantic import BaseModel

app = FastAPI()

class SlashCommandPayload(BaseModel):
    channel_id: str
   

def send_summary():
    summary = utils.create_summary()
    utils.send_msg(params.CHANNEL, summary)

@app.post("/summary")
async def trigger_endpoint(background_tasks: BackgroundTasks, payload: SlashCommandPayload):
    #Slack backslash expects a response in a 3 sec so we process on background
    # background_tasks.add_task(send_summary)
    
    channel_id = payload.channel_id
    return f"this was sent from {channel_id}"
    return Response(status_code=200)