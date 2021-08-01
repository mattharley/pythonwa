from typing import Optional

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import requests


app = FastAPI()

# allow cross origin access while in development
app.add_middleware(
    CORSMiddleware,
    allow_origins=['http://localhost:3000'],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get('/api/events/future')
def events_future():
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
