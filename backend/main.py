from typing import Optional

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import requests


class TalkApplication(BaseModel):
    name: str
    email: str
    topic: Optional[str] = None

app = FastAPI()

# allow cross origin access while in development
app.add_middleware(
    CORSMiddleware,
    allow_origins=['http://localhost:3000'],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get('/api/talks/future')
def talks_future():
    response = requests.get('https://api.meetup.com/Perth-Django-Users-Group/events/')
    if response.status_code == 200:
        data = response.json()
        sorted_data = sorted(data, key=lambda d: d['time'])
        events = []
        for event in sorted_data:
            events.append({
                'name': event['name'],
                'time': event['time'],
                'venue': event['venue'],
                'attendance': event['yes_rsvp_count'],
                'description': event['description'],
                'link': event['link'],
            })
    return events

@app.post('/api/talks/apply')
def talks_apply(application: TalkApplication):
    return application
