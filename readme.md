# Slack - Summary

This application provides a summary functionality triggered by the `/summary` command on Slack.

![slack-bot](https://s11.gifyu.com/images/Sutzy.gif)


## Installation

To install the application, follow these steps:

1. Clone the repository: `git clone https://github.com/jotaefe0/slack-summary.git`
2. Install the requirements: `pip install -r requirements.txt`

## Usage

- For local development run `uvicorn main:app`

### Railway Hosting

This application is hosted on Railway. To deploy the application on Railway, you need to follow these steps:

1. Sign up for a Railway account at https://railway.app
2. Connect your GitHub repository to Railway.
3. Configure the environment variables:
   - Set `OPENAI_API_KEY` to your OpenAI API key.
   - Set `SLACK_BOT_API_KEY` to your Slack bot API key.
4. Deploy the application using Railway's deployment feature.

### Adding Slack Bot to Channel

To use the `/summary` command, you need to create a Slack bot and add it to your channel. Follow these steps:

1. Go to the Slack API website: https://api.slack.com
2. Create a new Slack app.
3. Enable the "Slash Commands" feature for your app.
4. Set the Request URL to the endpoint URL where your app is hosted (e.g., `https://your-app-url.com/summary`).
5. Install the app to your workspace.
6. Go to your Slack workspace and navigate to the desired channel.
7. Click on the channel name and select "Invite team members to join..."
8. Search for the name of your Slack bot and click on it to add it to the channel.

## Environment Variables

Make sure to set the following environment variables:

- `OPENAI_API_KEY`: Your OpenAI API key.
- `SLACK_BOT_API_KEY`: Your Slack bot API key.

