import os
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError
from dotenv import load_dotenv
import params

load_dotenv()

###SLACK###

#connect to slack API
client = WebClient(token=os.environ['SLACK_BOT_TOKEN'])

#define functions
def send_msg(channel:str, text:str):
    """
    Send msg to selected slack channel
    channel: channel to send ex. #general
    text: msg to send as str

    returns status
    """
    try:
        response = client.chat_postMessage(channel=channel, text=text)
    except SlackApiError as e:
        # You will get a SlackApiError if "ok" is False
        assert e.response["ok"] is False
        assert e.response["error"]  # str like 'invalid_auth', 'channel_not_found'
        print(f"Got an error: {e.response['error']}")
    return response.status_code

def get_channels_ids():
    """
    returns a dict with name:id for every channel the bot has access
    """
    r = client.conversations_list()
    ids = {i['name']:i['id'] for i in r.data['channels']}
    return ids

def get_conversation_history(channel_id:str):
    """
    param: channel id
    returns a list of all msgs in a channel
    """

    # You can add the params as a feature in conversations_history
    # latest --> Only messages before this Unix timestamp will be included in results. Default is the current time.
    # oldest --> Only messages after this Unix timestamp will be included in results.
    response = client.conversations_history(channel=channel_id)
    return [message['text'] for message in response["messages"]]
    

###OPENAI###

import openai
import time
openai.api_key = os.environ['OPENAI_API_KEY']

def set_prompt(conversation_history):
    content= params.PROMPT.format(conversation_history=conversation_history)
    return content

def format_message(content):
    message = [
                {"role": "system", "content": params.CONTEXT},
                {"role": "user", "content": content}
                ]
    return message

def get_gpt_response(message):
    while True:
        try:
            response = openai.ChatCompletion.create(
              model=params.MODEL,
              temperature=params.TEMPERATURE,
              messages=message
            )
            break
        except openai.error.APIConnectionError as e:
            continue
        except openai.error.RateLimitError as e:
            time.sleep(0.5)
            continue
    return response


###MAIN###
def create_summary():
    ids = get_channels_ids()
    conversation_history = get_conversation_history(ids[params.CHANNEL])
    conversation_history = '\n'.join(conversation_history[::-1])
    prompt = set_prompt(conversation_history)
    message = format_message(prompt)
    r = get_gpt_response(message)

    return r['choices'][0]['message']['content']


