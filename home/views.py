from django.shortcuts import render_to_response
from django.utils.html import strip_tags
from django.utils import dateformat

import meetup.api
import datetime
import pytz

def get_events(event_status):
    client = meetup.api.Client('73c42797541a6c207a2a2b41262a66')

    group_info = client.GetGroup({'urlname': 'Perth-Django-Users-Group'})
    group_events = client.GetEvents({'group_id': group_info.id, 'status': event_status})

    return [
        (lambda event_datetime: {
            'group_id': group_info.id,
            'event_id': event['id'],
            'event_name': event['name'],
            'og_event_name': '({}) {}'.format(dateformat.format(event_datetime, 'D d M'), event['name']),
            'event_address': '{}, {}'.format(event['venue']['name'], event['venue']['address_1']),
            'event_description': event['description'],
            'og_event_description': strip_tags(event['description']).encode('ascii', 'ignore'),
            'event_yes_rsvp_count': event['yes_rsvp_count'],
            'event_datetime': event_datetime,
        })(datetime.datetime.fromtimestamp(event['time'] / 1000.0, pytz.timezone('Australia/Perth')))
        for event in reversed(group_events.results)
    ]

def home_page(request):
    try:
        coming_event = get_events('upcoming')[0]
    except IndexError:
        coming_event = {
            'event_name': 'No upcoming event',
            'event_description': 'Check back in the middle of the month',
            'og_event_description': 'Check back in the middle of the month',
        }
    return render_to_response(
        'home.html',
        {
            'coming_event': coming_event, 
        },
        # context_instance=RequestContext(request)
    )


def get_involved(request):
    return render_to_response(
        'getinvolved.html',
        {
        },

        # context_instance=RequestContext(request)
    )


def ajax_meetups_tab(request, event_status):
    """
    Queries the meetup.com API to get all the events of the status specified

    :param request:
    :param event_status: upcoming, past, proposed, suggested, cancelled, draft
    :return:
    """
    events = get_events(event_status)

    return render_to_response(
        'ajax/ajax_meetups.html',
        {
            "group_events": events,

            'event_status': event_status,
        })
