django-ab-testing
==================

Install:
```
pip install git+https://github.com/shantilabs/django-ab-testing#egg=ab_testing
```

settings.py
```python

INSTALLED_APPS = (
    # ...
    'ab_testing',
)

MIDDLEWARE_CLASSES = (
    # ...
    'ab_testing.middleware.AbTestingMiddleware',
)

# default value
AB_TESTING_SESSION_KEY = 'ab_testing'
AB_TESTING_CASES = {
    'h1_css_class': ['big', 'small', 'hidden'],
}
```

Templates:
```html
<body>
    {# split-test #}
    <h1 class="{{ request.session.ab_testing.h1_css_class }}">Title</h1>

    {# goal tracking #}
    <button onclick="goal('red_button_pressed')">Click here</button>

    {# yandex.metrika counter #}
    {% include "ab_testing/metrika.html" with yacounter_id=12345678 %}
</body>
```
