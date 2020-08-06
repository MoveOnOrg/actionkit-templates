import datetime
from . import lib

class subscriptions(list):
    list_ids = [1, 3, 7]


contexts = {
    'user_view.html': {
        'filename': 'user_view.html',
        'page': {
        'title': 'User self serve',
        'name': 'user view',
        },
    },
    'signup.html': {
        'filename': 'signup.html',
        'page': {
            'title': 'Signup!',
            'name': 'signup',
            "custom_fields": {
                "entity": "pac"
            }
        },
        'form': {
            'introduction_text': 'Signup now!',
            'user_fields': {
                'first_name': 'Ann'
            }
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
    'signup.smssubscribe': {
        'filename': 'signup.html',
        'page': {
            'title': 'Signup! sms-opt-out',
            'name': 'signup',
            "custom_fields": {
                "entity": "pac",
                "phone_mobile": "opt-out"
            }
        },
        'form': {
            'introduction_text': 'Signup now!',
            'user_fields': {
                'first_name': 'Ann'
            }
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
    'user_update.html': lib.userform({
        'filename': 'user_update.html',
        'page': {
            'title': 'Update Your Information',
            'name': 'user-update',
            "custom_fields": {
                "entity": "pac"
            },
            "followup": {
                "share_title": ""
            }
        },
        'user': lib.user({
                    "id": "7338",
                    "name": "George Costanza",
                    "phone": "515-555-0199",
        }),
    }, {  # form
        'introduction_text': 'Please update your information below',
        'user_fields': [
            {'field_name': 'email',
             'label_text': 'Email Address',
             'input_tag': '<input id="id_email" type="email" maxlength="255" name="email" />',
             },
            {'field_name': 'prefix',
             'label_text': 'Prefix',
             'input_tag': '<input id="id_prefix" type="text" maxlength="255" name="prefix" />',
             },
            {'field_name': 'first_name',
             'label_text': 'First name',
             'input_tag': '<input id="id_first_name" type="text" maxlength="255" name="first_name" />',
             },
            {'field_name': 'middle_name',
             'label_text': 'Middle name',
             'input_tag': '<input id="id_middle_name" type="text" maxlength="255" name="middle_name" />',
             },
            {'field_name': 'last_name',
             'label_text': 'Last name',
             'input_tag': '<input id="id_last_name" type="text" maxlength="255" name="last_name" />',
             },
            {'field_name': 'suffix',
             'label_text': 'Suffix',
             'input_tag': '<input id="id_suffix" type="text" maxlength="255" name="suffix" />',
             },
            {'field_name': 'country',
             'label_text': 'Country',
             'input_tag': lib.countries(),
             },
            {'field_name': 'address1',
             'label_text': 'Street Address',
             'input_tag': '<input id="id_address1" type="text" maxlength="255" name="address1" />',
             },
            {'field_name': 'address2',
             'label_text': 'Street Address',
             'input_tag': '<input id="id_address2" type="text" maxlength="255" name="address2" />',
             },
            {'field_name': 'city',
             'label_text': 'City',
             'input_tag': '<input id="id_city" type="text" maxlength="255" name="city" />',
             },
            {'field_name': 'state',
             'label_text': 'State',
             'input_tag': lib.states(),
             },
            {'field_name': 'zip',
             'label_text': 'Zip',
             'input_tag': '<input id="id_zip" type="text" maxlength="255" name="zip" />',
             },
            {'field_name': 'plus4',
             'label_text': 'Plus4',
             'input_tag': '<input id="id_plus4" type="text" maxlength="255" name="plus4" />',
             },
            {'field_name': 'region',
             'label_text': 'Region',
             'input_tag': '<input id="id_region" type="text" maxlength="255" name="region" />',
             },
            {'field_name': 'postal',
             'label_text': 'Postal Code',
             'input_tag': '<input id="id_postal" type="text" maxlength="255" name="postal" />',
             },
            {'field_name': 'lang',
             'label_text': 'Language',
             'input_tag': '<select id="id_lang" name="lang"><option value="">---------</option><option value="100" selected>English</option></select>',
             },
        ],
    }),
    'recurring_update.html': {
        'filename': 'recurring_update.html',
        'page': {
            'title': 'Update Account Information',
            'name': 'recurring_page',
            'custom_fields': {
                'proxypassword': 'abc123'
            }

        },
        'logged_in_user': {
            'name': 'Daddy Warbucks',
            'address1': 'Easy Street',
            'email': 'daddy.warbucks@example.com',
            'city': 'New York',
            'state': 'NY',
            'phone': '555-123-1233',
            'subscriptions': subscriptions([
                {'list_id': 1},
                {'list_id': 3},
                {'list_id': 7},
            ])
        },
        'active': [{  # profile
            'id': '123',
            'payment_processor_information': {
                'use_cse': False,
                'cse_key': '123123',
                'use_tr': True,
            },
            'status': 'active',  # get actual data
            'updated_at': datetime.datetime(2016, 1, 1),  # get actual data
            'created_at': datetime.datetime(2016, 1, 1),  # get actual data
            'start': datetime.datetime(2015, 1, 1),  # get actual data
            'payment_count': 10,
            'get_period_display': 'Monthly',  # get actual data
            'payment_total_amt': '$200.00',  # get actual data
            'amt': '$20',
            'order': {
                'payment_method': 'cc'
            },
            'card_num': '1234',
            'display_expiration_date': '05/2060',
            'next_payment_date': datetime.datetime(2016, 9, 1),
        }],
        'inactive': [],
    },
    'recurring_update_paypal': {
        'filename': 'recurring_update.html',
        'page': {
            'title': 'Update Account Information (PayPal)',
            'name': 'recurring_page',
        },
        'logged_in_user': {
            'name': 'Daddy Warbucks',
            'address1': 'Easy Street',
            'email': 'daddy.warbucks@example.com',
            'city': 'New York',
            'state': 'NY',
            'phone': '555-123-1233',
        },
        "show_paypal": True,
        "paypal_cohort": 0,
        'active': [{  # profile
            'id': '123',
            'payment_processor_information': {
                'use_cse': False,
                'cse_key': '123123',
                'use_tr': True,
            },
            'status': 'active',  # get actual data
            'updated_at': datetime.datetime(2016, 1, 1),  # get actual data
            'created_at': datetime.datetime(2016, 1, 1),  # get actual data
            'start': datetime.datetime(2015, 1, 1),  # get actual data
            'payment_count': 10,
            'get_period_display': 'Monthly',  # get actual data
            'payment_total_amt': '$200.00',  # get actual data
            'amt': '$20',
            'order': {
                'payment_method': 'paypal'
            },
            'card_num': '1234',
            'display_expiration_date': '05/2060',
            'next_payment_date': datetime.datetime(2016, 9, 1),
        }],
        'inactive': [],
    },
    'recurring_update_ach.html': {
        'filename': 'recurring_update.html',
        'page': {
            'title': 'Update Account Information (ACH)',
            'name': 'recurring_page',
            'custom_fields': {
                'proxypassword': 'abc123'
            }

        },
        'logged_in_user': {
            'name': 'Daddy Warbucks',
            'address1': 'Easy Street',
            'email': 'daddy.warbucks@example.com',
            'city': 'New York',
            'state': 'NY',
            'phone': '555-123-1233',
            'subscriptions': subscriptions([
                {'list_id': 1},
                {'list_id': 3},
                {'list_id': 7},
            ])
        },
        'active': [{  # profile
            'id': '123',
            'is_ach': True,
            'payment_processor_information': {
                'use_cse': False,
                'cse_key': '123123',
                'use_tr': True,
            },
            'status': 'active', #get actual data
            'updated_at': datetime.datetime(2016, 1, 1), #get actual data
            'created_at': datetime.datetime(2016, 1, 1), #get actual data
            'start': datetime.datetime(2015, 1, 1), #get actual data
            'payment_count': 10,
            'get_period_display': 'Monthly', #get actual data
            'payment_total_amt': '$200.00', #get actual data
            'amt': '$20',
            'order': {
                'payment_method': 'cc'
            },
            'card_num': '1234',
            'display_expiration_date': '05/2060',
            'next_payment_date': datetime.datetime(2016, 9, 1),
        }],
        'inactive': [],
    },
}
