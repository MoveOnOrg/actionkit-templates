"""
Scenarios:
1. single
2. args
     10 args.amount_other = "666"
     11 args.donation_type = "recurring", "single"
      2 args.payment_hash = "abc123"
      5 args.suggested_ask = "5", "666"

    All used together:
      1 args.recurring_start = ""
      1 args.suppress_duplicate_check
      1 args.action_upgrade_order_id
3. user
      1 user.custom_fields.employer
      1 user.custom_fields.occupation
4. args.proxy (DSG) with logged_in_user.akid
5. candidates (bundling)
6. pac/c4 (page variables)

Variables:
page.allow_international
page.currency_sym
page.custom_fields.donation_header
page.custom_fields.entity
page.custom_fields.layout_options
page.derived.currency_accounts
page.derived.use_account_switcher
page.has_candidates
page.id
page.name
page.payment_processor_information as pp
page.payment_processor_information.use_cse
page.payment_processor_information.use_tr
page.title
"""

import datetime

args_permutations = {
    "amount_other": ["666"],
    "donation_type": ["recurring", "single"],
    "payment_hash": ["abc123"],
    "suggested_ask": ["20", "666"],
}

def user(recurring=1, payment_hash=False, customfields=None):
    if not customfields:
        customfields = {
            "occupation": "witch",
            "employer": "self-employed",
        }
    userbase = {
        "user": {
            "akid": 666,
            "name": "Morticia Addams",
            "first_name": "Morticia",
            "last_name": "Addams",
            "address": "1313 Cemetery Lane",
            "city": "Westfield",
            "state": "NJ",
            "zip": "07091",
            "email": "morticia@example.com",
            "custom_fields": customfields,
        }
    }
    if payment_hash:
        userbase['user'].update({
            'payment_hash': 'abc123abc123',
            'has_payment_token': True,
        })
    userbase['user'].update({
            'orderrecurring_set': {
                'active': {
                    'count': recurring,
                },
                'count': recurring
            }
        })
    return userbase

candidates = {
    "has_candidates": True,
    "candidates": [
        {"name": "Seabright Cooley",
         "portrait_url": "https://fr.web.img2.acsta.net/medias/nmedia/18/35/61/70/19013441.jpg",
         "desc": "Seabright (Seab) Cooley from South Carolina and the book Advise and Consent",
         "id": "1959",
        }
    ]
}


def base(title='', entity='c4', layout='', filename="donate.html", fields={}):
    rv = {
        "filename": filename,
        "page": {
            "canonical_url": "https://example.actionkit.com/donate/give-me-the-money/",
            "type": "Donation",
            "custom_fields": {
                "layout_options": "2col,no_social,%s" % layout,
                "entity": entity, # "pac", "joint_pac_c4"
                #"thanks_header_text": "You are the best!", #optional
                #"sharing_prompt": False, #optional
            },
            "title": 'Donate to Example.com (%s)' % title,
            "name": "civ-donation",
            "id": 123,
            "currency_sym": "$",

        },
        "form": {
            "ask_text": "Contribute to Example.com (%s)" % title,
            "thank_you_text": """
              <p>You have successfully made your contribution. Thanks so much for your support!</p>
            """,
        },
    "amounts": [20,40,75,200,400,750,1500,"other"],
        "allow_monthly": True,
    }
    rv['page']['custom_fields'].update(fields)
    return rv

def order(order_type='order', details=None, quickpay=False):
    #order_type = 'orderrecurring'
    orderkey = {
        'order': {
            'id': 123456,
            'amt': '$12.07',
            'created_at': datetime.datetime.now(),
            'account': 'Example.com Civic Action',
        }
    }
    if order_type == 'orderrecurring':
        orderkey['orderrecurring'] = orderkey['order']
    if details:
        orderkey[order_type].update(details)
    rv = {
        'akid': '--userakidTEST--',
        'action': {
            'id': 654321,
            'custom_fields': {
                'upgrade_order_id': '111',
                'add_me_to_weekly': True, #optional
            },
        }
    }
    if quickpay:
        rv['action']['custom_fields'].update({
            'payment_token': 'abc123999',
        })
    rv.update(orderkey)
    rv['action'].update(orderkey)
    return rv

def compose(bases, argparams=[], argind=0):
    rv = dict()
    for b in bases:
        rv.update(b)
    arg_dict = dict([(k,args_permutations[k][argind]) for k in argparams])
    rv.update({'args': arg_dict})
    return rv

contexts = {
    'donate.1': compose([base('civ')]),
    'donate.2': compose([base('candidate', entity='pac'), candidates]),
    'donate.3': compose([base('suggested_ask')], ["suggested_ask",]),
    'donate.4': compose([base('suggested_ask, recurring')], ["suggested_ask","donation_type"]),
    'donate.5': compose([base('other suggested_ask, single')], ["suggested_ask","donation_type"], -1),
    'donate.6': compose([base('suggested_ask, payment_hash'), user(0, payment_hash=True)], ["suggested_ask","payment_hash"]),
    'donate.7': compose([base('user'), user()]),
    'donate.8': compose([base('pac', entity='pac')]),
    'donate.9': compose([base('candidate suggested', entity='pac', layout='donate_5050_split'), candidates], ["suggested_ask"], -1),
    
    'donate.thanks.1': compose([base('civ with payment_hash', filename='thanks.html'), user(0, payment_hash=True), order()]),
    'donate.thanks.2': compose([base('recurring civ', entity='pac', filename='thanks.html'),
                                user(), order('orderrecurring')]),
    'donate.thanks.3': compose([base('recurring civ receipt message',
                                     entity='pac', filename='thanks.html',
                                     fields={'thanks_below_receipt_message':'<b>This message is below the receipt!</b>'}
                                 ),
                                user(), order('orderrecurring')]),
    'donate.thanks.4': compose([base('recurring user recurring', filename='thanks.html'),
                                user(2), order('orderrecurring')]),
    'donate.thanks.5': compose([base('pac user payment_hash', entity='pac', filename='thanks.html'),
                                user(0, payment_hash=True), order()]),
    'donate.thanks.6': compose([base('pac user quickpay no employer', entity='pac', filename='thanks.html'),
                                user(0, payment_hash=True, customfields={'x':1}), order(quickpay=True)]),
    'donate.thanks.7': compose([base('pac user candidate', entity='pac', filename='thanks.html'),
                                user(0, payment_hash=True),
                                order(details={
                                    'order_details': [
                                        {'candidate': {'name': "Francis Underwood"},
                                         'amount': 10.00,},
                                    ],
                                    'other_amount': 2.07
                                })]),
    
}
