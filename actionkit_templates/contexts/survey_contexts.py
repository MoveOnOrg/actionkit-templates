from . import lib
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
        "name": "Morticia Addams",
        "first_name": "Morticia",
        "last_name": "Addams",
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

lost_pages_redesign = {
    'filename': 'survey.html',
    'page': {
        "title": "Change Do Not Mail Status",
        "canonical_url": "http://example.com/survey/foobar",
        "custom_fields": {
            "layout_options": ["lost_pages_redesign"]
        }
    },
    'form': {
        'introduction_text': 'Marking your account as "Do Not Mail" means MoveOn will not send you postal mail. (Your email address is required only to communicate with you if there are issues processing your opt-out—completing this form will not subscribe you to MoveOn\'s email list.)',
    },
    'user_fields': [
        {'field_name': 'email',
         'label_text': 'Email Address',
         'input_tag': '<input id="id_email" type="text" class="form-control mo-userfield-input ak-has-overlay"  name="email" />',
         'input_html': format_html('<input id="id_email" type="text" class="form-control mo-userfield-input ak-has-overlay"  name="email" />'),
        },
        {'field_name': 'user_postal_mail_status',
         'label_text': 'Postal Mail Status',
         'input_tag': lib.postal_mail_status(),
        },
        {'field_name': 'name',
         'label_text': 'Name',
         'input_tag': '<input id="id_name" type="text" class="form-control mo-userfield-input ak-has-overlay" name="name" />',
         'input_html': format_html('<input id="id_name" type="text" class="form-control mo-userfield-input ak-has-overlay" name="name" />'),
        },
        {'field_name': 'address1',
         'label_text': 'Street Address',
         'input_tag': '<input id="id_address1" type="text" class="form-control mo-userfield-input ak-has-overlay" />',
         'input_html': format_html('<input id="id_address1" type="text" class="form-control mo-userfield-input ak-has-overlay" />'),
        },
        {'field_name': 'state',
         'label_text': 'State',
         'input_tag': lib.states(),
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
    "user": {
        "akid": 666,
        "id": 666,
        "name": "Morticia Addams",
        "first_name": "Morticia",
        "last_name": "Addams",
    }
}
logged_in_data.update(survey)

contexts = {
    'survey.html': survey,
    'survey_logged_in': logged_in_data,
    'survey_logged_in_hide_recognized': logged_in_data_with_hide_recognized_block,
    'survey_no_questions': no_questions,
    'survey_no_survey': no_survey,
    'survey_lost-pages-redesign.html': lost_pages_redesign,
     #kinda silly, but avoid appending to the bottom because then git merge conflicts arise more often.
    #let's do the context values in alphabetical order.
}
