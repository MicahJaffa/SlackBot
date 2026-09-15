import os
from slack_bolt import App
from dotenv import load_dotenv

load_dotenv()
app = App(token=os.environ["SLACK_BOT_TOKEN"])

def post_jobs(jobs):
    
    channel = os.environ["CHANNEL_ID"]
    app.client.chat_postMessage(channel=channel, text="test")
    for job in jobs:
        message = (
            f" *New Job Alert!*\n"
            f" *Title:* {job.get('job_title', 'N/A')}\n"
            f" *Company:* {job.get('employer_name', 'N/A')}\n"
            f" *Location:* {job.get('job_city', 'N/A')}, {job.get('job_country', 'N/A')}\n"
            f" *Type:* {job.get('job_employment_type', 'N/A')}\n"
            f" *Apply:* {job.get('job_apply_link', 'N/A')}"
        )
        app.client.chat_postMessage(channel=channel, text=message)