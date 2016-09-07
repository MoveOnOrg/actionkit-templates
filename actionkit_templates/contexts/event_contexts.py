import datetime

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
            "title": "Page Title",
            "type": "Event",
        },
        "attendees": attendees,
        "cohosts": cohosts,
        "event": {
            "address1": "1 Main St.",
            "city_etc": "Somewhere, OH 44444",
            "directions": "Up up down down, left, then right, then left, then right. Press B A and then Select Start",
            "get_starts_at_display": "Monday, Jan 1, 1:00 AM",
            "is_in_past": False,
            "is_open_for_signup": True,
            "note_to_attendees": "Do hokey-pokey and turn yourself around.",
            "public_description": "Public description. Ipso lorem....",
            "title": "My Event Title",
            "venue": "Venue Name",
        },
        "campaign": {
            "local_title": "Campaign Title",
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
            "use_title": True,
            "show_venue": True,
            "show_title": True,
            "show_address1": True,
            "show_zip": True,
            "show_public_description": True,
        },
        "event": {
            "get_starts_at_display": "Saturday, August 20 at noon GMT",
            "obj": {
                "starts_at": datetime.datetime(2017, 12, 1, 1, 0, 0),
                "eventsignup_set": {
                    "all": [
                        {
                            "role": "host",
                            "user": user({
                                "first_name": "First",
                                "last_name": "Last",
                                "phone": "123-456-7890",
                            }),
                        },
                    ],
                },
            },
            "address1": "1 Main St.",
            "city_etc": "Somewhere, OH 44444",
            "directions": "Directions.",
            "get_starts_at_display": "Monday, Jan 1, 1:00 AM",
            "is_in_past": False,
            "is_open_for_signup": True,
            "note_to_attendees": "Note to attendees.",
            "public_description": "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.",
            "title": "Event Title",
            "venue": "Venue Name",
        },
        "events": [
            {
                "obj": {
                    "starts_at": datetime.datetime(2017, 12, 1, 1, 0, 0),
                    "eventsignup_set": {
                        "all": [
                            {
                                "role": "host",
                                "user": user({
                                    "first_name": "First",
                                    "last_name": "Last",
                                    "phone": "123-456-7890",
                                }),
                            },
                        ],
                    },
                },
                "address1": "1 Main St.",
                "city_etc": "Somewhere, OH 44444",
                "directions": "Directions.",
                "get_starts_at_display": "Monday, Jan 1, 1:00 AM",
                "is_in_past": False,
                "is_open_for_signup": True,
                "note_to_attendees": "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.",
                "public_description": "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.",
                "title": "Event Title",
                "venue": "Venue Name",
            },
        ],
        "form": {
            "signup_text": "<p>Signup text.</p>",
        },
        "page": {
            "title": "Page Title",
            "type": "Event",
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
            "use_title": True,
            "show_venue": True,
            "show_title": True,
            "show_address1": True,
            "show_zip": True,
            "show_public_description": True,
        },
        "event": {
            "obj": {
                "starts_at": datetime.datetime(2017, 12, 1, 1, 0, 0),
                "eventsignup_set": {
                    "all": [
                        {
                            "role": "host",
                            "user": user({
                                "first_name": "First",
                                "last_name": "Last",
                                "phone": "123-456-7890",
                            }),
                        },
                    ],
                },
            },
            "address1": "1 Main St.",
            "city_etc": "Somewhere, OH 44444",
            "directions": "Directions.",
            "get_starts_at_display": "Monday, Jan 1, 1:00 AM",
            "is_in_past": False,
            "is_open_for_signup": True,
            "note_to_attendees": "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.",
            "public_description": "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.",
            "title": "Event Title",
            "venue": "Venue Name",
        },
        "events": [
            {
                "obj": {
                    "starts_at": datetime.datetime(2017, 12, 1, 1, 0, 0),
                    "eventsignup_set": {
                        "all": [
                            {
                                "role": "host",
                                "user": user({
                                    "first_name": "First",
                                    "last_name": "Last",
                                    "phone": "123-456-7890",
                                }),
                            },
                        ],
                    },
                },
                "address1": "1 Main St.",
                "city_etc": "Somewhere, OH 44444",
                "directions": "Directions.",
                "get_starts_at_display": "Monday, Jan 1, 1:00 AM",
                "is_in_past": False,
                "is_open_for_signup": True,
                "note_to_attendees": "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.",
                "public_description": "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.",
                "title": "Event Title",
                "venue": "Venue Name",
            },
        ],
        "form": {
            "signup_text": "<p>Signup text.</p>",
        },
        "page": {
            "title": "Page Title",
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
            "search_page_text": "<p>Search page text.</p>",
        },
        "page": {
            "title": "Page Title",
        },
    },
    'event_search_with_results.html': {
        "filename": "event_search.html",
        "campaign": {
            "local_title": "Campaign Title",
            "use_title": True,
            "show_venue": True,
            "show_title": True,
            "show_zip": True,
            "show_public_description": True,
        },
        "events": [
            {
                "obj": {
                    "starts_at": datetime.datetime(2017, 12, 1, 1, 0, 0),
                    "eventsignup_set": {
                        "all": [
                            {
                                "role": "host",
                                "user": user({
                                    "first_name": "First",
                                    "last_name": "Last",
                                    "phone": "123-456-7890",
                                }),
                            },
                        ],
                    },
                },
                "address1": "1 Main St.",
                "city_etc": "Somewhere, OH 44444",
                "directions": "Directions.",
                "distance_str": "1 mile",
                "get_starts_at_display": "Monday, Jan 1, 1:00 AM",
                "is_in_past": False,
                "is_open_for_signup": True,
                "note_to_attendees": "Note to attendees.",
                "public_description": "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.",
                "starts_at": "Monday, Jan 1, 1:00 AM",
                "title": "Event Title",
                "venue": "Venue Name",
            },
        ],
        "form": {
            "search_page_text": "<p>Search page text.</p>",
        },
        "page": {
            "title": "Page Title",
        },
    },
    'event_create.html': {
        "filename": "event_create.html",
        'page': {
            "title": "March on Washington",
            "canonical_url": "http://example.com/"
        },
        'form': {
            'thank_you_text': '<p>Thanks!</p>'
        },
        'campaign': {
            'allow_private': True,
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
            "title": "March on Washington",
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
