from fastapi import FastAPI, Response
import utils
import params

app = FastAPI()

@app.post("/summary")
async def trigger_endpoint():
    summary = await utils.create_summary()
    utils.send_msg(params.CHANNEL, summary)
    return Response(status_code=200)