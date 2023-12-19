from django.utils.html import format_html

logged_in_data_with_hide_recognized_block = {
    "filename": "survey.html",
    "page": {
        "title": "Survey page (stub)",
        "canonical_url": "http://example.com/survey/foobar",
        "custom_fields": {
            "layout_options": "hide_recognized_block",
        },
    },
    "form": {
        "introduction_text": "Take our Survey!",
        "surveyquestion_set": {
            "all": [
                {"question_label": "How do you feel?",
                 "question_html": '<input type="text" name="action_howfeel" />',
                 "input_html": format_html('<input type="text" name="action_howfeel" />'),
                 "placeholder": "Share your feelings",
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
    "user_fields": [
        {"field_name": "name",
         "label_text": "Name",
         "input_tag": '<input id="id_name" type="text" class="form-control mo-userfield-input ak-has-overlay" name="name" />',
         "input_html": format_html('<input id="id_name" type="text" class="form-control mo-userfield-input ak-has-overlay" name="name" />'),
        },
        {"field_name": "email",
         "label_text": "Email Address",
         "input_tag": '<input id="id_email" type="text" class="form-control mo-userfield-input ak-has-overlay"  name="email" />',
         "input_html": format_html('<input id="id_email" type="text" class="form-control mo-userfield-input ak-has-overlay"  name="email" />'),
        },
        {"field_name": "address1",
         "label_text": "Street Address",
         "input_tag": '<input id="id_address1" type="text" class="form-control mo-userfield-input ak-has-overlay" />',
         "input_html": format_html('<input id="id_address1" type="text" class="form-control mo-userfield-input ak-has-overlay" />'),
        },
        {"field_name": "city",
         "label_text": "City",
         "input_tag": '<input id="id_city" type="text" class="form-control mo-userfield-input ak-has-overlay" name="city" />',
         "input_html": format_html('<input id="id_city" type="text" class="form-control mo-userfield-input ak-has-overlay" name="city" />'),
        },
        {"field_name": "state",
         "label_text": "State",
         "input_tag": '<input id="id_city" type="text" class="form-control mo-userfield-input ak-has-overlay" name="state" />',
         "input_html": format_html('<input id="id_state" type="text" class="form-control mo-userfield-input ak-has-overlay" name="state" />'),
        },
        {"field_name": "zip",
         "label_text": "ZIP Code",
         "input_tag": '<input id="id_zip" type="text" class="form-control mo-userfield-input ak-has-overlay" name="zip" />',
         "input_html": format_html('<input id="id_zip" type="text" class="form-control mo-userfield-input ak-has-overlay" name="zip" />'),
        },
        {"field_name": "phone",
         "label_text": "Phone",
         "input_tag": '<input id="id_phone" type="text" class="form-control mo-userfield-input ak-has-overlay" name="phone" />',
         "input_html": format_html('<input id="id_phone" type="text" class="form-control mo-userfield-input ak-has-overlay" name="phone" />'),
     },
    ],
}

no_questions = {
    "filename": "survey.html",
    "page": {
        "title": "Survey page (stub)",
        "canonical_url": "http://example.com/survey/foobar",
    },
    "form": {
        "introduction_text": "Take our Survey!",
        "surveyquestion_set": {
            "all": [],
        },
    },
    "user_fields": [
        {"field_name": "name",
         "label_text": "Name",
         "input_tag": '<input id="id_name" type="text" class="form-control mo-userfield-input ak-has-overlay" name="name" />',
         "input_html": format_html('<input id="id_name" type="text" class="form-control mo-userfield-input ak-has-overlay" name="name" />'),
        },
        {"field_name": "email",
         "label_text": "Email Address",
         "input_tag": '<input id="id_email" type="text" class="form-control mo-userfield-input ak-has-overlay"  name="email" />',
         "input_html": format_html('<input id="id_email" type="text" class="form-control mo-userfield-input ak-has-overlay"  name="email" />'),
        },
        {"field_name": "address1",
         "label_text": "Street Address",
         "input_tag": '<input id="id_address1" type="text" class="form-control mo-userfield-input ak-has-overlay" />',
         "input_html": format_html('<input id="id_address1" type="text" class="form-control mo-userfield-input ak-has-overlay" />'),
        },
        {"field_name": "zip",
         "label_text": "ZIP Code",
         "input_tag": '<input id="id_zip" type="text" class="form-control mo-userfield-input ak-has-overlay" name="zip" />',
         "input_html": format_html('<input id="id_zip" type="text" class="form-control mo-userfield-input ak-has-overlay" name="zip" />'),
        },
        {"field_name": "phone",
         "label_text": "Phone",
         "input_tag": '<input id="id_phone" type="text" class="form-control mo-userfield-input ak-has-overlay" name="phone" />',
         "input_html": format_html('<input id="id_phone" type="text" class="form-control mo-userfield-input ak-has-overlay" name="phone" />'),
     },
    ],
}

no_survey = {
    "filename": "survey.html",
    "page": {
        "title": "Survey page (stub)",
        "canonical_url": "http://example.com/survey/foobar",
        "custom_fields": {
            "layout_options": "nosurvey",
        },
    },
}

survey = {
    "filename": "survey.html",
    "page": {
        "title": "Survey page (stub)",
        "canonical_url": "http://example.com/survey/foobar",
    },
    "form": {
        "introduction_text": "Take our Survey!",
        "surveyquestion_set": {
            "all": [
                {"question_label": "How do you feel?",
                 "question_html": '<input type="text" name="action_howfeel" />',
                 "input_html": format_html('<input type="text" name="action_howfeel" />'),
                 "placeholder": "Share your feelings",
             },
            ],
        },
    },
    "user_fields": [
        {"field_name": "name",
         "label_text": "Name",
         "input_tag": '<input id="id_name" type="text" class="form-control mo-userfield-input ak-has-overlay" name="name" />',
         "input_html": format_html('<input id="id_name" type="text" class="form-control mo-userfield-input ak-has-overlay" name="name" />'),
        },
        {"field_name": "email",
         "label_text": "Email Address",
         "input_tag": '<input id="id_email" type="text" class="form-control mo-userfield-input ak-has-overlay"  name="email" />',
         "input_html": format_html('<input id="id_email" type="text" class="form-control mo-userfield-input ak-has-overlay"  name="email" />'),
        },
        {"field_name": "address1",
         "label_text": "Street Address",
         "input_tag": '<input id="id_address1" type="text" class="form-control mo-userfield-input ak-has-overlay" />',
         "input_html": format_html('<input id="id_address1" type="text" class="form-control mo-userfield-input ak-has-overlay" />'),
        },
        {"field_name": "city",
         "label_text": "City",
         "input_tag": '<input id="id_city" type="text" class="form-control mo-userfield-input ak-has-overlay" name="city" />',
         "input_html": format_html('<input id="id_city" type="text" class="form-control mo-userfield-input ak-has-overlay" name="city" />'),
        },
        {"field_name": "state",
         "label_text": "State",
         "input_tag": '<input id="id_city" type="text" class="form-control mo-userfield-input ak-has-overlay" name="state" />',
         "input_html": format_html('<input id="id_state" type="text" class="form-control mo-userfield-input ak-has-overlay" name="state" />'),
        },
        {"field_name": "zip",
         "label_text": "ZIP Code",
         "input_tag": '<input id="id_zip" type="text" class="form-control mo-userfield-input ak-has-overlay" name="zip" />',
         "input_html": format_html('<input id="id_zip" type="text" class="form-control mo-userfield-input ak-has-overlay" name="zip" />'),
        },
        {"field_name": "phone",
         "label_text": "Phone",
         "input_tag": '<input id="id_phone" type="text" class="form-control mo-userfield-input ak-has-overlay" name="phone" />',
         "input_html": format_html('<input id="id_phone" type="text" class="form-control mo-userfield-input ak-has-overlay" name="phone" />'),
     },
    ],
}

shipping_survey = {
    "filename": "survey.html",
    "page": {
        "title": "Shipping survey",
        "canonical_url": "http://example.com/survey/foobar",
    },
    "form": {
        "introduction_text": "verify shipping!",
        "surveyquestion_set": {
            "all": [
                {"question_label": "How do you feel?",
                 "question_html": '<input type="text" name="action_howfeel" />',
                 "input_html": format_html('<input type="text" name="action_howfeel" />'),
                 "placeholder": "Share your feelings",
                 "field_name": "howfeel",
             },
            {"question_label": "Address",
              "question_html": '<input type="text" name="action_shipping_address" />',
              "input_html": format_html('<input type="text" name="action_shipping_address" />'),
              "field_name": "shipping_address",
              },
              {"question_label": "Address Line 2",
               "question_html": '<input type="text" name="action_shipping_address2" />',
               "input_html": format_html('<input type="text" name="action_shipping_address2" />'),
               "field_name": "shipping_address2",
               },
               {"question_label": "City",
                "question_html": '<input type="text" name="action_shipping_city" />',
                "input_html": format_html('<input type="text" name="action_shipping_city" />'),
                "field_name": "shipping_city",
                },
                {"question_label": "zip",
                 "question_html": '<input type="text" name="action_shipping_zip" />',
                 "input_html": format_html('<input type="text" name="action_shipping_zip" />'),
                 "placeholder": "Share your feelings",
                 "field_name": "shipping_zip",
                 },
            ],
        },
    },
    "user_fields": [
        {"field_name": "name",
         "label_text": "Name",
         "input_tag": '<input id="id_name" type="text" class="form-control mo-userfield-input ak-has-overlay" name="name" />',
         "input_html": format_html('<input id="id_name" type="text" class="form-control mo-userfield-input ak-has-overlay" name="name" />'),
        },
        {"field_name": "email",
         "label_text": "Email Address",
         "input_tag": '<input id="id_email" type="text" class="form-control mo-userfield-input ak-has-overlay"  name="email" />',
         "input_html": format_html('<input id="id_email" type="text" class="form-control mo-userfield-input ak-has-overlay"  name="email" />'),
        },
        {"field_name": "address1",
         "label_text": "Street Address",
         "input_tag": '<input id="id_address1" type="text" class="form-control mo-userfield-input ak-has-overlay" />',
         "input_html": format_html('<input id="id_address1" type="text" class="form-control mo-userfield-input ak-has-overlay" />'),
        },
        {"field_name": "zip",
         "label_text": "ZIP Code",
         "input_tag": '<input id="id_zip" type="text" class="form-control mo-userfield-input ak-has-overlay" name="zip" />',
         "input_html": format_html('<input id="id_zip" type="text" class="form-control mo-userfield-input ak-has-overlay" name="zip" />'),
        },
        {"field_name": "phone",
         "label_text": "Phone",
         "input_tag": '<input id="id_phone" type="text" class="form-control mo-userfield-input ak-has-overlay" name="phone" />',
         "input_html": format_html('<input id="id_phone" type="text" class="form-control mo-userfield-input ak-has-overlay" name="phone" />'),
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
    },
}
logged_in_data.update(survey)

letter_to_congress_base = {
    "filename": "letter.html",
    "page": {
        "title": "Tell Letter to Congress",
        "goal": "100",
        "custom_fields": {
            "layout_options": "lost_pages_redesign",
        },
    },
    "form": {
        "statement_leadin": "<p>Hello, please sign our letter to congress for this very-good-cause.</p>",
        "letter_text": "Dear Senator,\n\nPlease listen to us?\nThis is very important.\nPlease listen to us?\nThis is very important.\nPlease listen to us?\nThis is very important.\nPlease listen to us?\nThis is very important.\nPlease listen to us?\nThis is very important.\nPlease listen to us?\nThis is very important.\nPlease listen to us?\nThis is very important.\nPlease listen to us?\nThis is very important.\nPlease listen to us?\nThis is very important.\nPlease listen to us?\nThis is very important.\nPlease listen to us?\nThis is very important.\nPlease listen to us?\nThis is very important.\nPlease listen to us?\nThis is very important.\nPlease listen to us?\nThis is very important.\nPlease listen to us?\nThis is very important.\nPlease listen to us?\nThis is very important.\nPlease listen to us?\nThis is very important.\nPlease listen to us?\nThis is very important.\nPlease listen to us?\nThis is very important.\nPlease listen to us?\nThis is very important.\nPlease listen to us?\nThis is very important.\nPlease listen to us?\nThis is very important.\nPlease listen to us?\nThis is very important.\nPlease listen to us?\nThis is very important.\nPlease listen to us?\nThis is very important.\nPlease listen to us?\nThis is very important.\nPlease listen to us?\nThis is very important.\nPlease listen to us?\nThis is very important.\nPlease listen to us?\nThis is very important.\nPlease listen to us?\nThis is very important.\nPlease listen to us?\nThis is very important.\nPlease listen to us?\nThis is very important.\nPlease listen to us?\nThis is very important.\nPlease listen to us?\nThis is very important.\nPlease listen to us?\nThis is very important.\nPlease listen to us?\nThis is very important.\nPlease listen to us?\nThis is very important.\nPlease listen to us?\nThis is very important.\nPlease listen to us?\nThis is very important.\nPlease listen to us?\nThis is very important.\nPlease listen to us?\nThis is very important.\nPlease listen to us?\nThis is very important.\nPlease listen to us?\nThis is very important.\nPlease listen to us?\nThis is very important.\nPlease listen to us?\nThis is very important.\nPlease listen to us?\nThis is very important.\nPlease listen to us?\nThis is very important.\nPlease listen to us?\nThis is very important.\nPlease listen to us?\nThis is very important.\nPlease listen to us?\nThis is very important.\nPlease listen to us?\nThis is very important.\nPlease listen to us?\nThis is very important.\nPlease listen to us?\nThis is very important.\nPlease listen to us?\nThis is very important.\nPlease listen to us?\nThis is very important.",
        "about_text": "This is what this thing is all about.",
    },
    "progress": {
        "goal": 100,
        "current": 90,
        "total": {
            "actions": 90,
        },
        "goal_type": "actions",
    },
    "context": {
        "progress": {"total": {"actions": 1}, "goal": 5, "goal_type": "actions", "recent": {"actions": 1}, "time": 1621261302.6000607, "age": 447.172566652298},
    },
}
letter_to_congress = {}
letter_to_congress_login = {}
letter_to_congress.update(survey)
letter_to_congress_login = {}
letter_to_congress_login.update(logged_in_data)
letter_to_congress.update(letter_to_congress_base)
letter_to_congress_login.update(letter_to_congress_base)

contexts = {
    "survey.html": survey,
    "shipping_survey.html": shipping_survey,
    "survey_logged_in": logged_in_data,
    "survey_logged_in_hide_recognized": logged_in_data_with_hide_recognized_block,
    "survey_no_questions": no_questions,
    "survey_no_survey": no_survey,
    "letter.html": letter_to_congress,
    "letter_logged_in": letter_to_congress_login,
     #kinda silly, but avoid appending to the bottom because then git merge conflicts arise more often.
    #let's do the context values in alphabetical order.
}
