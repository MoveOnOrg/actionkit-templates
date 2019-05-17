import csv
import datetime
import os
import random

from django.utils import timezone
from django.utils import dateformat
from django.utils.html import format_html

class signups(list):
    pass

class user(dict):

    def __str__(self):
        return self.get('name')

attendees = signups([
            # "role": "attendee",
            {
                #"role": "attendee",
                "user": user({
                    "id": "7338",
                    "name": "George Costanza",
                    "phone": "555-867-5309",
                }),
            },
            {
                #"role": "attendee",
                "user": user({
                    "id": "32799",
                    "name": "Mr. Signer-Upper",
                    "phone": "123-456-7890",
                }),
            },
        ])
attendees.role = 'attendee'

cohosts = signups([
            {
                #"role": "host",
                "user": user({
                    "id": "55555",
                    "name": "Ms. Hostly Host",
                    "phone": "123-456-7890",
                }),
            },
        ])
cohosts.role = 'host'

# 1000 based off of congressional district offices.  lat/lng are not accurate, but nearby
places_list = list(csv.DictReader(open(os.path.dirname(__file__) + '/event_places.csv')))

class MST(datetime.tzinfo):
    # use MST because AZ is in MST and doesn't observe DST
    def utcoffset(self, dt):
      return datetime.timedelta(hours=-7)
    def dst(self, dt):
        return datetime.timedelta(0)

def event_create(days_from_now=7, localtime=15, id=343775,
                 max_attendees=100, attendee_count=20,
                 is_inactive=False,
                 is_awaiting_confirmation=False,
                 place_index=None, minutes_from_now=False,
                 attend_page=False):

    """ 
        localtime = hour of the day
        To get an event time with more precision to the current time, 
        set days_from_now=0 and minutes_from_now to an integer, and
        choose a place_index with an MST locale.
    """
    now_utc = datetime.datetime.now(timezone.utc)

    if days_from_now == 0 and minutes_from_now:
        event_day = datetime.datetime.now(MST()) + datetime.timedelta(minutes = minutes_from_now)
        event_day = event_day.replace(tzinfo=timezone.FixedOffset(-420)) # matches MST
    else:
        today = datetime.date.today()
        event_day = datetime.datetime.combine(today + datetime.timedelta(days=days_from_now),
                                          datetime.time(localtime))
        event_day = event_day.replace(tzinfo=timezone.FixedOffset(-300))
    event_day_utc = event_day.astimezone(timezone.utc)
    place_loc = {}
    if place_index:
        place_loc = places_list[place_index]
    else:
        place_loc = places_list[random.randint(0, len(places_list) -1)]

    objobj = None
    if not attend_page:
        objobj = {
            "starts_at": event_day,
            "starts_at_utc": event_day_utc,
            "hosts": user({
                "first_name": "Host First",
                "last_name": "Host-Last",
                "phone": "123-456-7890",
            }),
        }
    evt_obj = {
        "id": id,
        "obj": objobj,
        "starts_at": event_day,
        "starts_at_utc": event_day_utc,
        "max_attendees": max_attendees,
        "attendee_count": attendee_count,

        # all overridden by place_loc
        "address1": "1 Main St.",
        "city": "Somewhere, OH 44444",
        # "longitude": 
        # "latitude": 

        "directions": "Directions.",
        "get_starts_at_display": dateformat.format(event_day, 'l, M j, g:i A'),  # "Monday, Jan 1, 1:00 AM",
        "is_in_past": bool(now_utc > event_day_utc),
        "is_full": bool(attendee_count >= max_attendees),
        "is_open_for_signup": bool(days_from_now > 0 and not attendee_count >= max_attendees),
        "is_inactive": is_inactive,
        "status": ("active" if not is_inactive else "cancelled"),
        "is_awaiting_confirmation": is_awaiting_confirmation,
        "note_to_attendees": "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.",
        "public_description": "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.",
        "title": "Event Title {}".format(place_index),
        "venue": "Venue Name",
    }
    evt_obj.update(place_loc)
    return evt_obj

contexts = {
    'event_host_tools.html': {
        "akid": "111111",
        "filename": "event_host_tools.html",
        "page": {
            "pagefollowup": {
                "send_taf": True,
            },
            "followup": {
                "taf_subject": "Come to my event!",
                "taf_body": "Hi, <a href='http://example.com/foo/bar/xyz'>blah blah</a> blah about the event!!<br />[[See the 'Tell-a-friend Body' in After-Action Info for the Host page of this event.]]"
            },
            "title": "Host Tools Page",
            "type": "Event",
            "name": "fakecampaign_create"
        },
        "attendees": attendees,
        "cohosts": cohosts,
        "event": event_create(),
        "campaign": {
            "local_title": "Campaign Title",
            "local_name": "fakecampaign_attend",
            "use_title": True,
        },
        "form": {
            "tools_text": """<p>Event host tools Page Intro text (see Edit content tab for Host section of event)
              Default is: "Thanks for creating your event! This page has all the information you need to make your event a success.  If you have any questions don't hesitate to email us."
            </p>
            """,
        },
        "signup": True,
        "user": user({
            "name": "Current user",
            "phone": "123-456-7890",
        }),
    },
    'event_attend.html': {
        "filename": "event_attend.html",
        "campaign": {
            "local_title": "Campaign Title",
            "local_name": "fakecampaign_attend",
            "use_title": True,
            "show_venue": True,
            "show_title": True,
            "show_address1": True,
            "show_zip": True,
            "show_public_description": True,
        },
        "event": event_create(place_index=20, attend_page=True),
        "events": [event_create(place_index=20)],
        "form": {
            "signup_text": "<p>Signup text.</p>",
            "ground_rules": "<p>Please follow these guidelines to ensure a good event:</p><ul><li>By RSVPing you agree to act non-violently and in accordance with the law.</li><li>Contact your host through this site to confirm the details of the event before you go.</li><li>Check this website if you have any questions.</li><li>If you've agreed to help the host, contact them through this site to coordinate with them.</li><li><em>Important Legal Note</em>:&nbsp;MoveOn.org Civic Action is an advocacy organization exempt from federal taxation under section 501(c)(4) of the Internal Revenue Code.</li></ul> "
        },
        "context": {
            "required": 'email'
        },
        'user_fields': [
            {'field_name': 'name',
             'label_text': 'Name',
             'input_tag': '<input id="id_name" type="text" class="form-control mo-userfield-input ak-has-overlay" name="name" />',
             'input_html': format_html('<input id="id_name" type="text" class="form-control mo-userfield-input ak-has-overlay" name="name" />'),
         },
            {'field_name': 'email',
             'label_text': 'Email Address',
             'input_tag': '<input id="id_email" type="text" class="form-control mo-userfield-input ak-has-overlay"  name="email" />',
             'input_html': format_html('<input id="id_email" type="text" class="form-control mo-userfield-input ak-has-overlay"  name="email" />'),
         },
            {'field_name': 'address1',
             'label_text': 'Street Address',
             'input_tag': '<input id="id_address1" type="text" class="form-control mo-userfield-input ak-has-overlay" />',
             'input_html': format_html('<input id="id_address1" type="text" class="form-control mo-userfield-input ak-has-overlay" />'),
         },
            {'field_name': 'zip',
             'label_text': 'ZIP Code',
             'input_tag': '<input id="id_zip" type="text" class="form-control mo-userfield-input ak-has-overlay" name="zip" />',
             'input_html': format_html('<input id="id_zip" type="text" class="form-control mo-userfield-input ak-has-overlay" name="zip" />'),
         },
            {'field_name': 'phone',
             'label_text': 'Phone',
             'input_tag': '<input id="id_phone" type="text" class="form-control mo-userfield-input ak-has-overlay" name="phone" />',
             'input_html': format_html('<input id="id_phone" type="text" class="form-control mo-userfield-input ak-has-overlay" name="phone" />'),
         },
        ],
        "page": {
            "title": "Event Attend (standard)",
            "type": "Event",
            "name": "fakecampaign_attend"
        },
        "logged_in_user":user({
            "name": "Current user",
            "phone": "123-456-7890",
        }),
        "user": user({
            "name": "Current user",
            "phone": "123-456-7890",
        }),
    },
    'event_attend_inactive.html': {
        "filename": "event_attend.html",
        "campaign": {
            "local_title": "Campaign Title",
            "local_name": "fakecampaign_attend",
            "use_title": True,
            "show_venue": True,
            "show_title": True,
            "show_address1": True,
            "show_zip": True,
            "show_public_description": True,
        },
        "event": event_create(place_index=20, is_inactive=True, attend_page=True),
        "events": [event_create(place_index=20, is_inactive=True)],
        "form": {
            "signup_text": "<p>Signup text.</p>",
            "ground_rules": "<p>Please follow these guidelines to ensure a good event:</p><ul><li>By RSVPing you agree to act non-violently and in accordance with the law.</li><li>Contact your host through this site to confirm the details of the event before you go.</li><li>Check this website if you have any questions.</li><li>If you've agreed to help the host, contact them through this site to coordinate with them.</li><li><em>Important Legal Note</em>:&nbsp;MoveOn.org Civic Action is an advocacy organization exempt from federal taxation under section 501(c)(4) of the Internal Revenue Code.</li></ul> "
        },
        "context": {
            "required": 'email'
        },
        'user_fields': [
            {'field_name': 'name',
             'label_text': 'Name',
             'input_tag': '<input id="id_name" type="text" class="form-control mo-userfield-input ak-has-overlay" name="name" />',
         },
            {'field_name': 'email',
             'label_text': 'Email Address',
             'input_tag': '<input id="id_email" type="text" class="form-control mo-userfield-input ak-has-overlay"  name="email" />',
         },
            {'field_name': 'address1',
             'label_text': 'Street Address',
             'input_tag': '<input id="id_address1" type="text" class="form-control mo-userfield-input ak-has-overlay" />',
         },
            {'field_name': 'zip',
             'label_text': 'ZIP Code',
             'input_tag': '<input id="id_zip" type="text" class="form-control mo-userfield-input ak-has-overlay" name="zip" />',
         },
            {'field_name': 'phone',
             'label_text': 'Phone',
             'input_tag': '<input id="id_phone" type="text" class="form-control mo-userfield-input ak-has-overlay" name="phone" />',
         },
        ],
        "page": {
            "title": "Event Attend (cancelled event)",
            "type": "Event",
            "name": "fakecampaign_attend"
        },
        "logged_in_user":user({
            "name": "Current user",
            "phone": "123-456-7890",
        }),
        "user": user({
            "name": "Current user",
            "phone": "123-456-7890",
        }),
    },
    'event_attend_past_event.html': {
        "filename": "event_attend.html",
        "campaign": {
            "local_title": "Campaign Title",
            "local_name": "fakecampaign_attend",
            "use_title": True,
            "show_venue": True,
            "show_title": True,
            "show_address1": True,
            "show_zip": True,
            "show_public_description": True,
        },
        "event": event_create(-2, place_index=20, attend_page=True),
        "events": [event_create(-2, place_index=20)],
        "form": {
            "signup_text": "<p>Signup text for past event.</p>",
            "ground_rules": "<p>Please follow these guidelines to ensure a good event:</p><ul><li>By RSVPing you agree to act non-violently and in accordance with the law.</li><li>Contact your host through this site to confirm the details of the event before you go.</li><li>Check this website if you have any questions.</li><li>If you've agreed to help the host, contact them through this site to coordinate with them.</li><li><em>Important Legal Note</em>:&nbsp;MoveOn.org Civic Action is an advocacy organization exempt from federal taxation under section 501(c)(4) of the Internal Revenue Code.</li></ul> "
        },
        "context": {
            "required": 'email'
        },
        'user_fields': [
            {'field_name': 'name',
             'label_text': 'Name',
             'input_tag': '<input id="id_name" type="text" class="form-control mo-userfield-input ak-has-overlay" name="name" />',
         },
            {'field_name': 'email',
             'label_text': 'Email Address',
             'input_tag': '<input id="id_email" type="text" class="form-control mo-userfield-input ak-has-overlay"  name="email" />',
         },
            {'field_name': 'address1',
             'label_text': 'Street Address',
             'input_tag': '<input id="id_address1" type="text" class="form-control mo-userfield-input ak-has-overlay" />',
         },
            {'field_name': 'zip',
             'label_text': 'ZIP Code',
             'input_tag': '<input id="id_zip" type="text" class="form-control mo-userfield-input ak-has-overlay" name="zip" />',
         },
            {'field_name': 'phone',
             'label_text': 'Phone',
             'input_tag': '<input id="id_phone" type="text" class="form-control mo-userfield-input ak-has-overlay" name="phone" />',
         },
        ],
        "page": {
            "title": "Event Attend (past event)",
            "type": "Event",
            "name": "fakecampaign_attend"
        },
        "logged_in_user":user({
            "name": "Current user",
            "phone": "123-456-7890",
        }),
        "user": user({
            "name": "Current user",
            "phone": "123-456-7890",
        }),
    },
    'event_attend_past_event_same_day.html': {
        "filename": "event_attend.html",
        "campaign": {
            "local_title": "Campaign Title",
            "local_name": "fakecampaign_attend",
            "use_title": True,
            "show_venue": True,
            "show_title": True,
            "show_address1": True,
            "show_zip": True,
            "show_public_description": True,
        },
        "event": event_create(0, 15, place_index=20, minutes_from_now=-20, attend_page=True),
        "events": [event_create(0, 15, place_index=20, minutes_from_now=-20)],
        "form": {
            "signup_text": "<p>Signup text for past event.</p>",
            "ground_rules": "<p>Please follow these guidelines to ensure a good event:</p><ul><li>By RSVPing you agree to act non-violently and in accordance with the law.</li><li>Contact your host through this site to confirm the details of the event before you go.</li><li>Check this website if you have any questions.</li><li>If you've agreed to help the host, contact them through this site to coordinate with them.</li><li><em>Important Legal Note</em>:&nbsp;MoveOn.org Civic Action is an advocacy organization exempt from federal taxation under section 501(c)(4) of the Internal Revenue Code.</li></ul> "
        },
        "context": {
            "required": 'email'
        },
        'user_fields': [
            {'field_name': 'name',
             'label_text': 'Name',
             'input_tag': '<input id="id_name" type="text" class="form-control mo-userfield-input ak-has-overlay" name="name" />',
         },
            {'field_name': 'email',
             'label_text': 'Email Address',
             'input_tag': '<input id="id_email" type="text" class="form-control mo-userfield-input ak-has-overlay"  name="email" />',
         },
            {'field_name': 'address1',
             'label_text': 'Street Address',
             'input_tag': '<input id="id_address1" type="text" class="form-control mo-userfield-input ak-has-overlay" />',
         },
            {'field_name': 'zip',
             'label_text': 'ZIP Code',
             'input_tag': '<input id="id_zip" type="text" class="form-control mo-userfield-input ak-has-overlay" name="zip" />',
         },
            {'field_name': 'phone',
             'label_text': 'Phone',
             'input_tag': '<input id="id_phone" type="text" class="form-control mo-userfield-input ak-has-overlay" name="phone" />',
         },
        ],
        "page": {
            "title": "Event Attend (past event same day)",
            "type": "Event",
            "name": "fakecampaign_attend"
        },
        "logged_in_user":user({
            "name": "Current user",
            "phone": "123-456-7890",
        }),
        "user": user({
            "name": "Current user",
            "phone": "123-456-7890",
        }),
    },
    'event_attendee_tools.html': {
        "akid": "111111",
        "filename": "event_attendee_tools.html",
        "campaign": {
            "local_title": "Campaign Title",
            "local_name": "fakecampaign_attend",
            "use_title": True,
            "show_venue": True,
            "show_title": True,
            "show_address1": True,
            "show_zip": True,
            "show_public_description": True,
        },
        "event": event_create(),
        "events": [event_create()],
        "form": {
            "signup_text": "<p>Signup text.</p>",
        },
        "page": {
            "title": "Event Attendee Tools",
            "name": "fakecampaign_attend",
            "type": "Event",
            "pagefollowup": {
                "send_taf": True,
            },
        },
        "signup": True,
        "logged_in_user":user({
            "name": "Current user",
            "phone": "123-456-7890",
        }),
        "user": user({
            "name": "Current user",
            "phone": "123-456-7890",
        }),
    },
    'event_search.html': {
        "filename": "event_search.html",
        "form": {
            "search_page_text": "<p>Search page text for campaign with only future events.</p>",
        },
        "page": {
            "title": "Event Search - Future Events Only",
            "name": "fakecampaign-with-future-events_attend"
        },
        "campaign": {
            "local_title": "Campaign Title for campaign with only future events",
            "local_name": "fakecampaign-with-future-events_attend",
            "use_title": True,
            "show_venue": True,
            "show_title": True,
            "show_zip": True,
            "show_public_description": True,
            "name": "fakecampaign-with-future-events",
            "public_create_page": True
        },
        "events": [event_create(1, 10, 343123),
                   event_create(1, 15, 343124),
                   event_create(4, 15, 343125),
                   event_create(0, 15, 343130, place_index=57, minutes_from_now=5)
               ],
    },
    'event_search_with_results': {
        "filename": "event_search.html",
        "args": {
            "page": "event_search"
        },
        "hide_map": False,
        "campaign": {
            "local_title": "Campaign Title for campaign with only future events",
            "local_name": "fakecampaign-with-future-events_attend",
            "use_title": True,
            "show_venue": True,
            "show_title": True,
            "show_zip": True,
            "show_public_description": True,
            "name": "fakecampaign-with-future-events", 
            "public_create_page": True
        },
        "events": [event_create(1, 10, 343123),
                   event_create(1, 15, 343124),
                   event_create(4, 15, 343125),
                   event_create(0, 15, 343130, place_index=57, minutes_from_now=5)
               ],
        "form": {
            "search_page_text": "<p>Search page text for campaign with only future events.</p>",
        },
        "page": {
            "title": "Event Search - with results",
            "name": "fakecampaign-with-future-events_attend"
        },
    },
    'event_search_with_results_showaddress1': {
        "filename": "event_search.html",
        "args": {
            "page": "event_search"
        },
        "hide_map": False,
        "campaign": {
            "local_title": "Campaign Title for campaign with only future events show_address1",
            "local_name": "fakecampaign-with-future-events_attend",
            "use_title": True,
            "show_venue": True,
            "show_title": True,
            "show_zip": True,
            "show_address1": True, # to support map in Original template
            "show_public_description": True,
            "name": "fakecampaign-with-future-events",
            "public_create_page": True
        },
        "events": [event_create(1, 10, 343123),
                   event_create(1, 15, 343124),
                   event_create(4, 15, 343125),
                   event_create(0, 15, 343130, place_index=57, minutes_from_now=5)
               ],
        "form": {
            "search_page_text": "<p>Search page text for campaign with only future events.</p>",
        },
        "page": {
            "title": "Event Search - with results",
            "name": "fakecampaign-with-future-events_attend"
        },
    },
    'event_search_noevents.html': {
        # this doesn't render as expected - come back to this later
        "filename": "event_search.html",
        "form": {
            "search_page_text": "<p>Search page text for campaign with no events.</p>",
        },
        "page": {
            "title": "Event Search - Campaign with no events",
            "name": "fakecampaign-with-no-events_attend"
        },
        "campaign": {
            "local_title": "Campaign Title - no events",
            "local_name": "fakecampaign-with-no-events",
            "use_title": True,
            "show_venue": True,
            "show_title": True,
            "show_zip": True,
            "show_public_description": True,
            "name": "fakecampaign-with-no-events",
            "public_create_page": True
        },
    },
    'event_search_with_no_results': {
        "filename": "event_search.html",
        "args": {
            "page": "event_search"
        },
        "campaign": {
            "local_title": "Campaign Title - no events",
            "local_name": "fakecampaign-with-no-events",
            "use_title": True,
            "show_venue": True,
            "show_title": True,
            "show_zip": True,
            "show_public_description": True,
            "name": "fakecampaign-with-no-events"
        },
        "events": [],
        "form": {
            "search_page_text": "<p>Search page text for campaign with no events.</p>",
        },
        "page": {
            "title": "Event Search - no results",
            "name": "fakecampaign-with-no-events_attend"
        },
    },
    'event_search_past_events_only.html': {
        "filename": "event_search.html",
        "form": {
            "search_page_text": "<p>Search page text for campaign with only past events.</p>",
        },
        "page": {
            "title": "Event Search - Past Events Only",
            "name": "fakecampaign-past-events-only_attend"
        },
        "events": [event_create(-1, 10, 343126),
                   event_create(-7, 15, 343127),
                   event_create(-5, 15, 343128),
                   event_create(0, 15, 343129, place_index=57, minutes_from_now=-5)
               ],
        "campaign": {
            "local_title": "Campaign Title",
            "local_name": "fakecampaign-past-events-only_attend",
            "use_title": True,
            "show_venue": True,
            "show_title": True,
            "show_zip": True,
            "show_public_description": True,
            "name": "resistandwin-volunteerday"
        },
    },
    'event_search_with_results_past_events_only': {
        "filename": "event_search.html",
        "args": {
            "page": "event_search"
        },
        "campaign": {
            "local_title": "Campaign Title",
            "local_name": "fakecampaign-past-events-only_attend",
            "use_title": True,
            "show_venue": True,
            "show_title": True,
            "show_zip": True,
            "show_public_description": True,
            "name": "resistandwin-volunteerday"
        },
        "events": [event_create(-1, 10, 343126),
                   event_create(-7, 15, 343127),
                   event_create(-5, 15, 343128),
                   event_create(0, 15, 343129, place_index=57, minutes_from_now=-5)
               ],
        "form": {
            "search_page_text": "<p>Search page text for campaign with only past events.</p>",
        },
        "page": {
            "title": "Event Search - with only past events in results",
            "name": "fakecampaign_attend"
        },
    },
    'event_search_past_and_future_events.html': {
        "filename": "event_search.html",
        "form": {
            "search_page_text": "<p>Search page text for campaign with past and future events.</p>",
        },
        "page": {
            "title": "Event Search - Past and Future Events",
            "name": "fakecampaign-past-and_future_events_attend"
        },
        "events": [event_create(-1, 10, 343126),
                   event_create(-7, 15, 343127),
                   event_create(-5, 15, 343128),
                   event_create(1, 15, 343123),
                   event_create(3, 15, 343124),
                   event_create(3, 10, 343125)
               ],
        "campaign": {
            "local_title": "Campaign Title - Campaign with past and future events",
            "local_name": "fakecampaign-past-and_future_events_attend",
            "use_title": True,
            "show_venue": True,
            "show_title": True,
            "show_zip": True,
            "show_public_description": True,
            "name": "resistandwin-volunteerday"
        },
    },
    'event_search_with_results_past_and_future_events': {
        "filename": "event_search.html",
        "args": {
            "page": "event_search"
        },
        "campaign": {
            "local_title": "Campaign Title",
            "local_name": "fakecampaign-past-and_future_events_attend",
            "use_title": True,
            "show_venue": True,
            "show_title": True,
            "show_zip": True,
            "show_public_description": True,
            "name": "resistandwin-volunteerday"
        },
        "events": [event_create(-1, 10, 343126),
                   event_create(-7, 15, 343127),
                   event_create(-5, 15, 343128),
                   event_create(1, 15, 343123),
                   event_create(3, 15, 343124),
                   event_create(3, 10, 343125)
               ],
        "form": {
            "search_page_text": "<p>Search page text for campaign with only past events.</p>",
        },
        "page": {
            "title": "Event Search - Past and Future Events",
            "name": "fakecampaign_attend"
        },
    },
    'event_search_with_api_broken': {
        "500_API": True,
        "filename": "event_search.html",
        "args": {
            "page": "event_search"
        },
        "campaign": {
            "local_title": "Campaign Title - no events",
            "local_name": "fakecampaign-with-no-events",
            "use_title": True,
            "show_venue": True,
            "show_title": True,
            "show_zip": True,
            "show_public_description": True,
            "name": "fakecampaign-with-no-events"
        },
        "events": [],
        "form": {
            "search_page_text": "<p>Search page text for campaign with no events.</p>",
        },
        "page": {
            "title": "Event Search - API Failure (should gracefully degrade)",
            "name": "fakecampaign-with-no-events_attend"
        },
    },
    'event_search_with_mueller_load.html': {
        "filename": "event_search.html",
        "form": {
            "search_page_text": "<p>Search page text for campaign with 1000 events.</p>",
        },
        "page": {
            "title": "Event Search - A Mueller Load of Events",
            "name": "fakecampaign-mueller_load_events_attend"
        },
        "events": [event_create(1, 17, 10000+place, place_index=place) for place in range(1000)],
        "campaign": {
            "local_title": "Campaign Title - Campaign with a Mueller Load of events",
            "local_name": "fakecampaign-mueller_load_events_attend",
            "use_title": True,
            "show_venue": True,
            "show_title": True,
            "show_zip": True,
            "show_public_description": True,
            "name": "fakecampaign-mueller_load_events"
        },
    },
    'event_search_with_mueller_load_past.html': {
        "filename": "event_search.html",
        "args": {
            "page": "event_search"
        },
        "campaign": {
            "local_title": "Campaign Title",
            "local_name": "fakecampaign-mueller_load_events_attend",
            "use_title": True,
            "show_venue": True,
            "show_title": True,
            "show_zip": True,
            "show_public_description": True,
            "name": "fakecampaign-mueller_load_events"
        },
        "events": [event_create(0, 17, 10000+place, place_index=place, minutes_from_now=-(place*2)) for place in range(1000)],
        "form": {
            "search_page_text": "<p>Search page text for campaign with only past events.</p>",
        },
        "page": {
            "title": "Event Search - Mueller Load of Events all in Past",
            "name": "fakecampaign_attend"
        },
    },
    'event_search_with_mueller_load_slow_api.html': {
        "SLOW_API": True,
        "filename": "event_search.html",
        "form": {
            "search_page_text": "<p>Search page text for campaign with 1000 events.</p>",
        },
        "page": {
            "title": "Event Search - A Mueller Load of Events (slow api race test)",
            "name": "fakecampaign-mueller_load_events_attend"
        },
        "events": [event_create(1, 17, 10000+place, place_index=place) for place in range(1000)],
        "campaign": {
            "local_title": "Campaign Title - Campaign with a Mueller Load of events",
            "local_name": "fakecampaign-mueller_load_events_attend",
            "use_title": True,
            "show_venue": True,
            "show_title": True,
            "show_zip": True,
            "show_public_description": True,
            "name": "fakecampaign-mueller_load_events"
        },
    },
    'event_search_with_mueller_load_slow_search.html': {
        "SLOW_SEARCH": True,
        "filename": "event_search.html",
        "form": {
            "search_page_text": "<p>Search page text for campaign with 1000 events.</p>",
        },
        "page": {
            "title": "Event Search - A Mueller Load of Events (slow search race test)",
            "name": "fakecampaign-mueller_load_events_attend"
        },
        "events": [event_create(1, 17, 10000+place, place_index=place) for place in range(1000)],
        "campaign": {
            "local_title": "Campaign Title - Campaign with a Mueller Load of events",
            "local_name": "fakecampaign-mueller_load_events_attend",
            "use_title": True,
            "show_venue": True,
            "show_title": True,
            "show_zip": True,
            "show_public_description": True,
            "name": "fakecampaign-mueller_load_events"
        },
    },
    'event_create.html': {
        "filename": "event_create.html",
        'page': {
            "title": "Event Creation - March on Washington",
            "canonical_url": "http://example.com/"
        },
        'form': {
            'thank_you_text': '<p>Thanks!</p>'
        },
        'campaign': {
            'allow_private': True,
            "local_title": "Campaign Title",
            "use_title": True,
            "show_venue": True,
            "show_title": True,
            "show_address1": True,
            "show_zip": True,
            "show_public_description": True
        },
        'event_starts_at': {
            'name': 'event_starts_at',
            'hidden_date': False,
            'static_date': False,
            'default_date': False, #could be text of date
            'hidden_time': False,
            'static_time': False,
            'default_time': '10:00',
            'default_ampm': 'AM',
        },
        'user_fields': [
            {'field_name': 'name',
             'label_text': 'Name',
             'input_tag': '<input id="id_name" type="text" class="form-control mo-userfield-input ak-has-overlay" name="name" />',
         },
            {'field_name': 'email',
             'label_text': 'Email Address',
             'input_tag': '<input id="id_email" type="text" class="form-control mo-userfield-input ak-has-overlay"  name="email" />',
         },
            {'field_name': 'address1',
             'label_text': 'Street Address',
             'input_tag': '<input id="id_address1" type="text" class="form-control mo-userfield-input ak-has-overlay" />',
         },
            {'field_name': 'zip',
             'label_text': 'ZIP Code',
             'input_tag': '<input id="id_zip" type="text" class="form-control mo-userfield-input ak-has-overlay" name="zip" />',
         },
            {'field_name': 'phone',
             'label_text': 'Phone',
             'input_tag': '<input id="id_phone" type="text" class="form-control mo-userfield-input ak-has-overlay" name="phone" />',
         },
        ],
    },
    'event_create-updating': {
        "filename": "event_create.html",
        'update': True,
        'logged_in_user': {
            'akid': 34563841,
            'name': 'Stephen King',
            'first_name': 'Stephen',
            'last_name': 'King',
            'address1': 'Elm Street',
            'city': 'Denver',
            'state': 'CO',
            'zip': "80210",
        },
        'args': {
            'update': 1,
        },
        'page': {
            "title": "Event Creation - update existing event",
            "canonical_url": "http://example.com/",
            'custom_fields': {
                'survey_always_show_user_fields': "1",
            }
        },
        'form': {
            'thank_you_text': '<p>Thanks!</p>'
        }
    },
}
