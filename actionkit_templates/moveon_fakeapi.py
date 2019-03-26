import time


def mo_event_data(event):
    eobj = event.get('obj')
    starts_utc = int(time.mktime(eobj['starts_at_utc'].timetuple()))
    timezone_offset = int((time.mktime(eobj['starts_at'].timetuple()) - starts_utc) / 60 / 60)
    full = 0 if not event['max_attendees'] else int(bool(event['max_attendees'] <= event['attendee_count']))
    return {'lat': float(event['latitude']),
            'lng': float(event['longitude']),
            'id': event['id'],
            'utc': starts_utc,
            'tzo': timezone_offset,
            'f': full,
            # this is not a perfect reflection of the api, but we are lazy so we send titles with the main batch
            'title': event['title']}
