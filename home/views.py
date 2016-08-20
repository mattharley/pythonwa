from django.shortcuts import render_to_response


def home_page(request):
    return render_to_response(
        'home.html',
        {
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

    import meetup.api
    import datetime
    import pytz

    client = meetup.api.Client('73c42797541a6c207a2a2b41262a66')

    group_info = client.GetGroup({'urlname': 'Perth-Django-Users-Group'})
    group_events = client.GetEvents({'group_id': group_info.id, 'status': event_status})

    array_event = []

    for event in group_events.results:
        perth_tz = pytz.timezone('Australia/Perth')

        event_datetime = event['time'] / 1000.0

        my_date_in_perth = datetime.datetime.fromtimestamp(event_datetime, perth_tz).strftime('%Y-%m-%d %H:%M:%S')

        # Convert datetime string to datetime object. This allows us to leverage 'humanize' within the template and display the dates in a more friendly way.
        my_date_in_perth = datetime.datetime.strptime(my_date_in_perth, '%Y-%m-%d %H:%M:%S')

        array_event.append({
            'group_id': group_info.id,
            'event_id': event['id'],
            'event_name': event['name'],
            'event_address': event['venue']['address_1'],
            'event_description': event['description'],
            'event_yes_rsvp_count': event['yes_rsvp_count'],
            'event_datetime': my_date_in_perth
        })

    return render_to_response(
        'ajax/ajax_meetups.html',
        {
            "group_info": group_info.__dict__.keys(),
            "group_name": group_info.name,
            "group_id": group_info.id,
            "group_events": array_event,

            'event_count': len(group_events.results),
            'event_status': event_status,
        })
