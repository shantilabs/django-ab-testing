import random
from django.conf import settings


AB_TESTING_SESSION_KEY = getattr(settings, 'AB_TESTING_SESSION_KEY', 'ab_testing')
AB_TESTING_CASES = getattr(settings, 'AB_TESTING_CASES', {})


class AbTestingMiddleware(object):
    def process_request(self, request):
        ab = request.session.setdefault(AB_TESTING_SESSION_KEY, {})

        # drop old keys
        for k in set(ab) - set(AB_TESTING_CASES):
            ab.pop(k, None)

        for k, choices in AB_TESTING_CASES.items():
            val = ab.get(k)
            if not val in choices:
                ab[k] = random.choice(choices)
