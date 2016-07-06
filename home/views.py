from django.shortcuts import render
import meetup.api
import datetime
import time
from pytz import timezone
import pytz

# Create your views here.


def home_page(request):
	
	client = meetup.api.Client('6d5355616d7145c43415a7a384f2c1d');

	group_info = client.GetGroup({'urlname': 'Perth-Django-Users-Group'})
	group_events = client.GetEvents({ 'group_id': group_info.id , 'status' :  'upcoming'   })

	keys = ['group_id','event_id','event_name','event_address','event_description','event_yes_rsvp_count', 'event_datetime']
	array_event = []

	for event in group_events.results: 
		perth_tz = pytz.timezone('Australia/Perth')
		my_date_in_perth =  datetime.datetime.fromtimestamp(event['time']/1000.0, perth_tz ).strftime('%Y-%m-%d %H:%M:%S') 
		array_event.append({'group_id': group_info.id, 'event_id': event['id'], 'event_name': event['name'], 'event_address': event['venue']['address_1'], 'event_description': event['description'], 'event_yes_rsvp_count' : event['yes_rsvp_count'], 'event_datetime': my_date_in_perth   })
		
	
	context = {
		"title":    "Upcoming Events",
		"tabtitle": "",
		"group_info":     group_info.__dict__.keys(),
		"group_name":     group_info.name,
		"group_id":     group_info.id,
		"group_events": array_event

	}

	return render(request, "home-index.html", context)