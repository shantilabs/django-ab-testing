from distutils.core import setup


setup(
    name='django-ab-testing',
    version='1.0',
    author='Maxim Oransky',
    author_email='maxim.oransky@gmail.com',
    url='https://github.com/shantilabs/django-ab-testing',
    packages=[
        'ab_testing'
    ],
    package_data={
        'public_id': ['templates/*'],
    },
)
