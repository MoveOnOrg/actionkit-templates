from django.utils.html import format_html

logged_in_data_with_hide_recognized_block = {
    'filename': 'survey.html',
    'page': {
        "title": "Survey page (stub)",
        "canonical_url": "http://example.com/survey/foobar",
        "custom_fields": {
            "layout_options": "hide_recognized_block",
        },
    },
    'form': {
        'introduction_text': 'Take our Survey!',
        'surveyquestion_set': {
            'all': [
                {'question_label': "How do you feel?",
                 'question_html': '<input type="text" name="action_howfeel" />',
                 'input_html': format_html('<input type="text" name="action_howfeel" />'),
                 'placeholder': 'Share your feelings',
             },
            ],
        },
    },
    "logged_in_user": {
        "akid": 666,
        "id": 666,
        "name": "Stephen King",
        "first_name": "Stephen",
        "last_name": "King",
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
        {'field_name': 'city',
         'label_text': 'City',
         'input_tag': '<input id="id_city" type="text" class="form-control mo-userfield-input ak-has-overlay" name="city" />',
         'input_html': format_html('<input id="id_city" type="text" class="form-control mo-userfield-input ak-has-overlay" name="city" />'),
        },
        {'field_name': 'state',
         'label_text': 'State',
         'input_tag': '<input id="id_city" type="text" class="form-control mo-userfield-input ak-has-overlay" name="state" />',
         'input_html': format_html('<input id="id_state" type="text" class="form-control mo-userfield-input ak-has-overlay" name="state" />'),
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
}

no_questions = {
    'filename': 'survey.html',
    'page': {
        "title": "Survey page (stub)",
        "canonical_url": "http://example.com/survey/foobar"
    },
    'form': {
        'introduction_text': 'Take our Survey!',
        'surveyquestion_set': {
            'all': [],
        },
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
}

no_survey = {
    'filename': 'survey.html',
    'page': {
        "title": "Survey page (stub)",
        "canonical_url": "http://example.com/survey/foobar",
        "custom_fields": {
            "layout_options": "nosurvey",
        },
    },
}

survey = {
    'filename': 'survey.html',
    'page': {
        "title": "Survey page (stub)",
        "canonical_url": "http://example.com/survey/foobar"
    },
    'form': {
        'introduction_text': 'Take our Survey!',
        'surveyquestion_set': {
            'all': [
                {'question_label': "How do you feel?",
                 'question_html': '<input type="text" name="action_howfeel" />',
                 'input_html': format_html('<input type="text" name="action_howfeel" />'),
                 'placeholder': 'Share your feelings',
             },
            ],
        },
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
        {'field_name': 'city',
         'label_text': 'City',
         'input_tag': '<input id="id_city" type="text" class="form-control mo-userfield-input ak-has-overlay" name="city" />',
         'input_html': format_html('<input id="id_city" type="text" class="form-control mo-userfield-input ak-has-overlay" name="city" />'),
        },
        {'field_name': 'state',
         'label_text': 'State',
         'input_tag': '<input id="id_city" type="text" class="form-control mo-userfield-input ak-has-overlay" name="state" />',
         'input_html': format_html('<input id="id_state" type="text" class="form-control mo-userfield-input ak-has-overlay" name="state" />'),
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
}

shipping_survey = {
    'filename': 'survey.html',
    'page': {
        "title": "Shipping survey",
        "canonical_url": "http://example.com/survey/foobar"
    },
    'form': {
        'introduction_text': 'verify shipping!',
        'surveyquestion_set': {
            'all': [
                {'question_label': "How do you feel?",
                 'question_html': '<input type="text" name="action_howfeel" />',
                 'input_html': format_html('<input type="text" name="action_howfeel" />'),
                 'placeholder': 'Share your feelings',
                 'field_name': 'howfeel',
             },
            {'question_label': "Address",
              'question_html': '<input type="text" name="action_shipping_address" />',
              'input_html': format_html('<input type="text" name="action_shipping_address" />'),
              'field_name': 'shipping_address',
              },
              {'question_label': "Address Line 2",
               'question_html': '<input type="text" name="action_shipping_address2" />',
               'input_html': format_html('<input type="text" name="action_shipping_address2" />'),
               'field_name': 'shipping_address2',
               },
               {'question_label': "City",
                'question_html': '<input type="text" name="action_shipping_city" />',
                'input_html': format_html('<input type="text" name="action_shipping_city" />'),
                'field_name': 'shipping_city',
                },
                {'question_label': "zip",
                 'question_html': '<input type="text" name="action_shipping_zip" />',
                 'input_html': format_html('<input type="text" name="action_shipping_zip" />'),
                 'placeholder': 'Share your feelings',
                 'field_name': 'shipping_zip',
                 },
            ],
        },
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
}

logged_in_data = {
    "logged_in_user": {
        "akid": 666,
        "id": 666,
        "name": "Stephen King",
        "first_name": "Stephen",
        "last_name": "King",
    },
    'user_context': {
        'name': 'Stephen King',
    }
}

akid_data = {
    "user": {
        "akid": 666,
        "id": 666,
        "name": "Morticia Addams",
        "first_name": "Morticia",
        "last_name": "Addams",
    },
    'user_context': {
        'name': 'Morticia Addams',
    },
    'incomplete': False  ## for letter_to_editor: indicating that we still need to submit the changes
}

survey_logged_in = {}
survey_logged_in.update(survey)
survey_logged_in.update(logged_in_data)


survey_logged_in_requiredfield = {}
survey_logged_in_requiredfield.update(survey_logged_in)
survey_logged_in_requiredfield.update({
    'user_context': {
        'name': 'Morticia Addams',
        'move_fields': ['phone']
    }
})

letter_to_congress_base = {
    'filename': 'letter.html',
    'page': {
        'title': 'Tell Letter to Congress',
        'goal': '100',
        'custom_fields': {
            'layout_options': 'lost_pages_redesign'
        }
    },
    'form': {
        'statement_leadin': '<p>Hello, please sign our letter to congress for this very-good-cause.</p>',
        'letter_text': 'Dear Senator,\n\nPlease listen to us?\nThis is very important.\nPlease listen to us?\nThis is very important.\nPlease listen to us?\nThis is very important.\nPlease listen to us?\nThis is very important.\nPlease listen to us?\nThis is very important.\nPlease listen to us?\nThis is very important.\nPlease listen to us?\nThis is very important.\nPlease listen to us?\nThis is very important.\nPlease listen to us?\nThis is very important.\nPlease listen to us?\nThis is very important.\nPlease listen to us?\nThis is very important.\nPlease listen to us?\nThis is very important.\nPlease listen to us?\nThis is very important.\nPlease listen to us?\nThis is very important.\nPlease listen to us?\nThis is very important.\nPlease listen to us?\nThis is very important.\nPlease listen to us?\nThis is very important.\nPlease listen to us?\nThis is very important.\nPlease listen to us?\nThis is very important.\nPlease listen to us?\nThis is very important.\nPlease listen to us?\nThis is very important.\nPlease listen to us?\nThis is very important.\nPlease listen to us?\nThis is very important.\nPlease listen to us?\nThis is very important.\nPlease listen to us?\nThis is very important.\nPlease listen to us?\nThis is very important.\nPlease listen to us?\nThis is very important.\nPlease listen to us?\nThis is very important.\nPlease listen to us?\nThis is very important.\nPlease listen to us?\nThis is very important.\nPlease listen to us?\nThis is very important.\nPlease listen to us?\nThis is very important.\nPlease listen to us?\nThis is very important.\nPlease listen to us?\nThis is very important.\nPlease listen to us?\nThis is very important.\nPlease listen to us?\nThis is very important.\nPlease listen to us?\nThis is very important.\nPlease listen to us?\nThis is very important.\nPlease listen to us?\nThis is very important.\nPlease listen to us?\nThis is very important.\nPlease listen to us?\nThis is very important.\nPlease listen to us?\nThis is very important.\nPlease listen to us?\nThis is very important.\nPlease listen to us?\nThis is very important.\nPlease listen to us?\nThis is very important.\nPlease listen to us?\nThis is very important.\nPlease listen to us?\nThis is very important.\nPlease listen to us?\nThis is very important.\nPlease listen to us?\nThis is very important.\nPlease listen to us?\nThis is very important.\nPlease listen to us?\nThis is very important.\nPlease listen to us?\nThis is very important.\nPlease listen to us?\nThis is very important.\nPlease listen to us?\nThis is very important.\nPlease listen to us?\nThis is very important.',
        'about_text': 'This is what this thing is all about.',
    },
    'progress': {
        'goal': 100,
        'current': 90,
        'total': {
            'actions': 90
        },
        'goal_type': 'actions'
    },
    'context': {
        "progress": {"total": {"actions": 1}, "goal": 5, "goal_type": "actions", "recent": {"actions": 1}, "time": 1621261302.6000607, "age": 447.172566652298},
    }
}
letter_to_congress = {}
letter_to_congress_login = {}
letter_to_congress.update(survey)
# remove city/state
letter_to_congress['user_fields'].pop(3)
letter_to_congress['user_fields'].pop(3) # was 4
letter_to_congress_login = {}
letter_to_congress_login.update(akid_data)
letter_to_congress.update(letter_to_congress_base)
letter_to_congress_login.update(letter_to_congress_base)

##################
# LETTER TO EDITOR
##################
media_targets = {
    "national": [{"id": 797, "name": "Wall Street Journal", "phone": "(212) 416-2000", "circulation": 2294000, "website_url": "http://www.wsj.com/", "sent": 0}, {"id": 336, "name": "USA Today", "phone": "(703) 854-3400", "circulation": 1674000, "website_url": "http://www.usatoday.com", "sent": 0}, {"id": 2088, "name": "Houston Chronicle", "phone": "(713) 362-7171", "circulation": 1042000, "website_url": "http://www.chron.com", "sent": 0}, {"id": 1862, "name": "The Daily Beast", "phone": "(212) 314-7300", "circulation": 0, "website_url": "http://www.thedailybeast.com", "sent": 0}, {"id": 1916, "name": "HuffPost", "phone": "(212) 652-6400", "circulation": 0, "website_url": "http://www.huffpost.com", "sent": 0}],
    "regional": [{"id": 401, "name": "New York Post", "phone": "(212) 930-8000", "circulation": 477000, "website_url": "http://www.nypost.com", "sent": 0}, {"id": 2029, "name": "Philadelphia Inquirer", "phone": "(215) 854-4500", "circulation": 477000, "website_url": "http://www.philly.com/inquirer", "sent": 0}, {"id": 2143, "name": "New York Daily News", "phone": "(212) 210-2100", "circulation": 456000, "website_url": "http://www.nydailynews.com", "sent": 0}, {"id": 307, "name": "Newsday (New York)", "phone": "(631) 843-2700", "circulation": 443000, "website_url": "http://www.newsday.com", "sent": 0}, {"id": 2023, "name": "The Star-Ledger", "phone": "(732) 902-4500", "circulation": 296000, "website_url": "http://www.nj.com/starledger", "sent": 0}],
    "local": [{"id": 2168, "name": "Korea Daily - New York", "phone": "(718) 361-7700", "circulation": 59000, "website_url": "http://www.koreadaily.com/index.html?branch=NY", "sent": 0}, {"id": 1586, "name": "Sing Tao Daily", "phone": "(212) 431-9030", "circulation": 55000, "website_url": "http://www.nysingtao.com", "sent": 0}, {"id": 1953, "name": "Ming Pao Free Daily", "phone": "(718) 786-2888", "circulation": 35000, "website_url": "http://www.mingpaony.com", "sent": 0}, {"id": 2173, "name": "Nowy Dziennik", "phone": "(212) 594-2266", "circulation": 28000, "website_url": "http://www.dziennik.com", "sent": 0}, {"id": 2099, "name": "Brooklyn Eagle", "phone": "(718) 422-7400", "circulation": 10000, "website_url": "http://www.brooklyneagle.com", "sent": 0}]
}


letter_to_editor_base = {
    'filename': 'lte.html',
    'page': {
        'title': "That's how you get Ants",
        'name': 'ants-letter',
        'goal': '100',
        'custom_fields': {
            'layout_options': 'lost_pages_redesign'
        }
    },
    'letter': {
        'id': 123,
        'subject': "Don't leave food out in the kitchen",
        'letter_text': "",
    },
    'form': {
        'introduction_text': '<p>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco</p><p> laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum</p>',
        'talking_points': '<div>Some Talking points<ul><li>Healthcare is a human right</li><li>Housing is a human right</li></ul></div>',
        'cannedletter_set': {
            'all': [
                {'id': 12345, 'subject': 'Ants subject 1', 'letter_text': 'Lorem ipsum 1'},
                {'id': 12345, 'subject': 'Ants subject 2', 'letter_text': 'Lorem ipsum 2'}
            ]
        }
    },
    'progress': {
        'goal': 100,
        'current': 90,
        'total': {
            'actions': 90
        },
        'goal_type': 'actions'
    },
    'incomplete': True, # for logged-out version (will be overridden by logged_in_data above for logged_in page example)
    'context': {
        "progress": {"total": {"actions": 1}, "goal": 5, "goal_type": "actions", "recent": {"actions": 1}, "time": 1621261302.6000607, "age": 447.172566652298},
    },
    'user_context': {
        "mediaTargets": media_targets,
        "show_phones": True,
        'name': 'Morticia Addams',

    }
}

letter_to_editor = {}
letter_to_editor.update(survey) # for user form fields
letter_to_editor.update(letter_to_editor_base)


letter_to_editor_login = {}
letter_to_editor_login.update(akid_data)
letter_to_editor_login.update(letter_to_editor_base)
letter_to_editor_login['incomplete'] = False

contexts = {
    'survey.html': survey,
    'shipping_survey.html': shipping_survey,
    'survey_logged_in': survey_logged_in,
    'survey_logged_in_hide_recognized': logged_in_data_with_hide_recognized_block,
    'survey_logged_in_requiredfield': survey_logged_in_requiredfield,
    'survey_no_questions': no_questions,
    'survey_no_survey': no_survey,
    'letter.html': letter_to_congress,
    'letter_logged_in': letter_to_congress_login,
    'lte.html': letter_to_editor,
    'letter_to_editor_logged_in': letter_to_editor_login,
     #kinda silly, but avoid appending to the bottom because then git merge conflicts arise more often.
    #let's do the context values in alphabetical order.
}
