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

def smartystreets_data():
    return [{
        "input_index": 0,
        "candidate_index": 0,
        "delivery_line_1": "1 Santa Claus Ln",
        "last_line": "North Pole AK 99705-9901",
        "delivery_point_barcode": "997059901010",
        "components": {
            "primary_number": "1",
            "street_name": "Santa Claus",
            "street_suffix": "Ln",
            "city_name": "North Pole",
            "state_abbreviation": "AK",
            "zipcode": "99705",
            "plus4_code": "9901",
            "delivery_point": "01",
            "delivery_point_check_digit": "0"
        },
        "metadata": {
            "record_type": "S",
            "zip_type": "Standard",
            "county_fips": "02090",
            "county_name": "Fairbanks North Star",
            "carrier_route": "C004",
            "congressional_district": "AL",
            "rdi": "Commercial",
            "elot_sequence": "0001",
            "elot_sort": "A",
            "latitude": 64.75233,
            "longitude": -147.35297,
            "precision": "Zip8",
            "time_zone": "Alaska",
            "utc_offset": -9,
            "dst": "true"
        },
        "analysis": {
            "dpv_match_code": "Y",
            "dpv_footnotes": "AABB",
            "dpv_cmra": "N",
            "dpv_vacant": "N",
            "active": "Y",
            "footnotes": "L#"
        }
    }]
        #                 "dst": true
    #             },
    #
    #         },
    #     ]}
