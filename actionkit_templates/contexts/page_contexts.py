import account_contexts
import donation_contexts
import event_contexts
import survey_contexts

contexts = {
    'base': {
        'thanks.html': {
            'filename': 'thanks.html',
            'page': {
                "title": "Thanks, you are the best",
                "canonical_url": "http://example.com/"
            },
            'form': {
                'thank_you_text': '<p>Thanks!</p>'
            }
        },
        'logout.html': {
            'filename': 'logout.html'
        }
    }
    #kinda silly, but avoid appending to the bottom because then git merge conflicts arise more often.
    #let's do the context values in alphabetical order.
}

contexts.update({'donations': donation_contexts.contexts})
contexts.update({'events': event_contexts.contexts})
contexts.update({'accounts': account_contexts.contexts})
contexts.update({'surveys': survey_contexts.contexts})
