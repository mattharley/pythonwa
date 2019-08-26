from django.shortcuts import render_to_response
from django.utils.html import strip_tags
from django.utils import dateformat
from django.utils import timezone

from itertools import zip_longest

import meetup.api
from meetup.exceptions import HttpClientError
import datetime
import pytz

perth_timezone = pytz.timezone('Australia/Perth')


def get_events(event_status, from_date):
    try:
        client = meetup.api.Client('73c42797541a6c207a2a2b41262a66')

        group_info = client.GetGroup({'urlname': 'Perth-Django-Users-Group'})
        try:
            group_events = client.GetEvents({'group_id': group_info.id, 'status': event_status}).results
        except ValueError:
            group_events = []

        iterable = (
            (lambda event_datetime: {
                'group_id': group_info.id,
                'event_id': event['id'],
                'event_name': event['name'],
                'event_url': event['event_url'],
                'og_event_name': '({}) {}'.format(dateformat.format(event_datetime, 'D d M'), event['name']),
                'event_address': '{}, {}'.format(event['venue']['name'], event['venue']['address_1']) if 'venue' in event else '',
                'event_description': event['description'],
                'og_event_description': strip_tags(event['description']).encode('ascii', 'ignore'),
                'event_yes_rsvp_count': event['yes_rsvp_count'],
                'event_datetime': event_datetime,
            })(datetime.datetime.fromtimestamp(event['time'] / 1000.0, perth_timezone))
            for event in sorted(group_events, key=lambda d: d['time']))
        return [
            event
            for event in iterable
            if event['event_datetime'] >= from_date
        ]
    except HttpClientError:
        return []


def home_page(request):
    date_str = ''.join(list(request.GET.keys())).strip()
    if date_str:
        now = timezone.now()
        default_args = (now.year, now.month, 1)
        user_args = list(map(int, date_str.split('-')))
        args = tuple(
            user_num or default
            for default, user_num in zip_longest(default_args, user_args))
        date = datetime.datetime(*args, tzinfo=perth_timezone)
    else:
        date = timezone.now()
    try:
        coming_event = get_events('upcoming', date)[0]
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
    events = get_events(event_status, timezone.now())

    return render_to_response(
        'ajax/ajax_meetups.html',
        {
            "group_events": events,

            'event_status': event_status,
        })
