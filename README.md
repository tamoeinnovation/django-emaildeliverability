# Emaildeliverability

A Django app that help monitoring systems to ensure that emails reach their intended destination.

## Installation

Use the package manager pip to install Emaildeliverability.

```
pip install django-emaildeliverability
```

## Quick start

1. Set the following variables in your settings.py (replace the values with your own):

```
EMAIL_DELIVERABILITY = {
    'USER': 'email@example.com',
    'PASSWORD': 'mysecretpassword',
    'SERVER': 'mail.example.com' # Imap server,
    'TIMEOUT': 45 # Optional. Time, in seconds, during which the app will try to verify that the email has reached its destination
    'INTERVAL': 5 # Optional. Retry interval
}
```

1. Add "emaildeliverability" to your INSTALLED_APPS setting like this:

```
    INSTALLED_APPS = [
        ...,
        "emaildeliverability",
    ]
```

2. Include the emaildeliverability URLconf in your project urls.py like this:

```
    path("emaildeliverability/", include("emaildeliverability.urls")),
```

3. Point your prefered monitoring tool to http://localhost:8000/emaildeliverability/check (replace localhost:8000 with your host:port). The request will return the text 'OK' and a status of 200 if the email reached the destination mailbox before TIMEOUT seconds, or 'KO' and a status of 400 otherwise.



