import datetime
import logging
from itertools import zip_longest
from typing import Optional, List

import meetup.api
import pytz
import requests
from cachetools import TTLCache, cached
from django.shortcuts import render
from django.utils import dateformat, timezone
from django.utils.html import strip_tags
from meetup.exceptions import HttpClientError

PERTH_TIMEZONE = pytz.timezone("Australia/Perth")
MEETUP_EVENTS_URL = "https://api.meetup.com/Perth-Django-Users-Group/events/"


logger = logging.getLogger(__name__)


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
def get_meetups() -> Optional[List[dict]]:
    """ get all the upcomming meetup events """
    results = None  # return None only if the request fails
    try:
        response = requests.get(MEETUP_EVENTS_URL)
        if response.status_code == 200:
            data = response.json()
            data = sorted(data, key=lambda d: d["time"])
            results = []
            for event in data:
                try:
                    venue = ""
                    if event.get("venue"):
                        venue = f"{event['venue']['name']}"
                        if event["venue"].get("address1"):
                            venue = f"{venue}, {event['venue']['address_1']}"
                    event_datetime = timezone.datetime.fromtimestamp(event["time"] / 1000.0, PERTH_TIMEZONE)
                    og_event_name = f"({dateformat.format(event_datetime, 'D d M')}) {event['name']}"
                    results.append(
                        {
                            "event_id": event["id"],
                            "event_name": event["name"],
                            "event_url": event["link"],
                            "og_event_name": og_event_name,
                            "event_address": venue,
                            "event_description": event["description"],
                            "og_event_description": str(strip_tags(event["description"]).encode("ascii", "ignore")),
                            "event_yes_rsvp_count": event["yes_rsvp_count"],
                            "event_datetime": event_datetime,
                        }
                    )
                except KeyError as e:
                    logger.exception(e)

    except requests.exceptions.RequestException as e:
        print(e)  # need to log this somehow
        logger.exception(e)
    return results


def home_page(request):
    # bendog - removed all of these lines because they are no longer needed and they were raising 500s
    # # TODO: bendog - this makes absolutely no sense, and i'm not sure why all GET.keys() are being loaded
    # get_args = [x for x in request.GET.keys() if x not in ('fbclid')]   # bendog - remove facebook link id
    # # TODO: bendog - this should probably be a allow list of allowed keys, not a deny list
    # date_str = "".join(get_args).strip()
    # if date_str:
    #     now = timezone.now()
    #     default_args = (now.year, now.month, 1)
    #     user_args = list(map(int, date_str.split("-")))
    #     args = tuple(user_num or default for default, user_num in zip_longest(default_args, user_args))
    #     date = datetime.datetime(*args, tzinfo=PERTH_TIMEZONE)
    # else:
    #     date = timezone.now()
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

    return render(request, "ajax/ajax_meetups.html", {"group_events": events, "event_status": event_status})
