import time


def mo_event_data(event):
    eobj = event.get('obj')
    machine_offset = time.time() - time.mktime(time.gmtime()) # correction factor for when this runs on machines that aren't defaulting to UTC
    naive_start_time = int(time.mktime(eobj['starts_at_utc'].timetuple()))
    starts_utc = naive_start_time + machine_offset
    timezone_offset = (int(time.mktime(eobj['starts_at'].timetuple())) - naive_start_time) / 3600
    full = 0 if not event['max_attendees'] else int(bool(event['max_attendees'] <= event['attendee_count']))
    return {'lat': float(event['latitude']),
            'lng': float(event['longitude']),
            'id': event['id'],
            'utc': starts_utc,
            'tzo': timezone_offset,
            'f': full,
            # this is not a perfect reflection of the api, but we are lazy so we send titles with the main batch
            'city_etc': '{}, {}'.format(event['city'], event['state']),
            'title': event['title']}
