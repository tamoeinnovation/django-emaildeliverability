=====
django-emaildeliverability
=====

django-emaildeliverability is a Django app to conduct web-based polls. For each question,
visitors can choose between a fixed number of answers.

Detailed documentation is in the "docs" directory.

Quick start
-----------

1. Add "polls" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = [
        ...,
        "emaildeliverability",
    ]

2. Include the polls URLconf in your project urls.py like this::

    path("emaildeliverability/", include("emaildeliverability.urls")),

3. Run ``python manage.py migrate`` to create the emaildeliverability models.

4. Set the following variables in settings:
EMAIL_DELIVERABILITY_USER = 'email@domain.com'
EMAIL_DELIVERABILITY_PASSWORD = 'mysecretpassword'
EMAIL_DELIVERABILITY_SERVER = 'mail.domain.com' # Email imap server
