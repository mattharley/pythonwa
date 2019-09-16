import requests
from cachetools import cached, TTLCache
from django.shortcuts import render
from django.utils.html import strip_tags
from django.utils import dateformat
from django.utils import timezone

from itertools import zip_longest

import meetup.api
from meetup.exceptions import HttpClientError
import datetime
import pytz

PERTH_TIMEZONE = pytz.timezone("Australia/Perth")
MEETUP_EVENTS_URL = "https://api.meetup.com/Perth-Django-Users-Group/events/"


# def get_events(event_status, from_date):
#     try:
#         client = meetup.api.Client('73c42797541a6c207a2a2b41262a66')
#
#         group_info = client.GetGroup({'urlname': 'Perth-Django-Users-Group'})
#         try:
#             group_events = client.GetEvents({'group_id': group_info.id, 'status': event_status}).results
#         except ValueError:
#             group_events = []
#
#         iterable = (
#             (lambda event_datetime: {
#                 'group_id': group_info.id,
#                 'event_id': event['id'],
#                 'event_name': event['name'],
#                 'event_url': event['event_url'],
#                 'og_event_name': '({}) {}'.format(dateformat.format(event_datetime, 'D d M'), event['name']),
#                 'event_address': '{}, {}'.format(event['venue']['name'], event['venue']['address_1']) if 'venue' in event else '',
#                 'event_description': event['description'],
#                 'og_event_description': strip_tags(event['description']).encode('ascii', 'ignore'),
#                 'event_yes_rsvp_count': event['yes_rsvp_count'],
#                 'event_datetime': event_datetime,
#             })(datetime.datetime.fromtimestamp(event['time'] / 1000.0, PERTH_TIMEZONE))
#             for event in sorted(group_events, key=lambda d: d['time']))
#         return [
#             event
#             for event in iterable
#             if event['event_datetime'] >= from_date
#         ]
#     except HttpClientError:
#         return []


@cached(cache=TTLCache(maxsize=1024, ttl=60 * 15))  # cache for 15 minutes
def get_meetups():
    """ get all the upcomming meetup events """
    results = None  # return None only if the request fails
    try:
        response = requests.get(MEETUP_EVENTS_URL)
        if response.status_code == 200:
            results = [
                {
                    "event_id": event["id"],
                    "event_name": event["name"],
                    "event_url": event["link"],
                    "og_event_name": "({}) {}".format(
                        dateformat.format(
                            datetime.datetime.fromtimestamp(
                                event["time"] / 1000.0, PERTH_TIMEZONE
                            ),
                            "D d M",
                        ),
                        event["name"],
                    ),
                    "event_address": "{}, {}".format(
                        event["venue"]["name"], event["venue"]["address_1"]
                    )
                    if "venue" in event
                    else "",
                    "event_description": event["description"],
                    "og_event_description": strip_tags(event["description"]).encode(
                        "ascii", "ignore"
                    ),
                    "event_yes_rsvp_count": event["yes_rsvp_count"],
                    "event_datetime": timezone.datetime.fromtimestamp(event["time"] / 1000.0),
                }
                for event in sorted(response.json(), key=lambda d: d["time"])
            ]

    except requests.exceptions.RequestException as e:
        print(e)  # need to log this somehow
    return results


def home_page(request):
    date_str = "".join(list(request.GET.keys())).strip()
    if date_str:
        now = timezone.now()
        default_args = (now.year, now.month, 1)
        user_args = list(map(int, date_str.split("-")))
        args = tuple(
            user_num or default for default, user_num in zip_longest(default_args, user_args)
        )
        date = datetime.datetime(*args, tzinfo=PERTH_TIMEZONE)
    else:
        date = timezone.now()
    try:
        # coming_event = get_events('upcoming', date)[0]
        coming_event = get_meetups()[0]
    except (IndexError, AttributeError):
        coming_event = {
            "event_name": "No upcoming event",
            "event_description": "Check back in the middle of the month",
            "og_event_description": "Check back in the middle of the month",
        }
    return render(
        request,
        "home.html",
        {"coming_event": coming_event},
        # context_instance=RequestContext(request)
    )


def get_involved(request):
    return render(
        request,
        "getinvolved.html",
        {},
        # context_instance=RequestContext(request)
    )


def ajax_meetups_tab(request, event_status):
    """
    Queries the meetup.com API to get all the events of the status specified

    :param request:
    :param event_status: upcoming, past, proposed, suggested, cancelled, draft
    :return:
    """
    # events = get_events(event_status, timezone.now())
    events = get_meetups()

    return render(
        request, "ajax/ajax_meetups.html", {"group_events": events, "event_status": event_status}
    )
