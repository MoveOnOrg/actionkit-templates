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
             },
            ],
        },
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

     #kinda silly, but avoid appending to the bottom because then git merge conflicts arise more often.
    #let's do the context values in alphabetical order.
}


