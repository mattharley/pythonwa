from typing import Optional

from fastapi import FastAPI
import requests


app = FastAPI()

@app.get('/events/future')
def events_future():
    response = requests.get('https://api.meetup.com/Perth-Django-Users-Group/events/')
    if response.status_code == 200:
        data = response.json()
        sorted_data = sorted(data, key=lambda d: d['time'])
        events = []
        for event in sorted_data:
            event_time = event['time']
            events.append({
                'name': event['name'],
                'time': event_time,
                'venue': event['venue'],
                'attendance': event['yes_rsvp_count'],
                'description': event['description'],
                'link': event['link'],
            })
    return events
