from datetime import datetime
from django.core.mail import EmailMessage
from django.conf import settings
from django.http import HttpResponse
from imap_tools import MailBox, AND
from loguru import logger
import time


def send_email_test(to, subject, cco=None, extra=None):
    mail = EmailMessage(
        subject=subject,
        body="test",
        from_email=settings.DEFAULT_FROM_EMAIL,
        to=[to],
        reply_to=[settings.DEFAULT_FROM_EMAIL],
    )
    mail.send()


def emaildeliverability(request):
    now = datetime.now()
    dt_string = now.strftime("%Y%m%d%H%M%S")

    subject = f"____DELIVERABILITY____{dt_string}"
    logger.debug(f"Sending with subject: {subject}")
    send_email_test(settings.EMAIL_DELIVERABILITY_USER, subject)

    t_end = time.time() + 45
    while time.time() < t_end:
        with MailBox(settings.EMAIL_DELIVERABILITY_SERVER).login(
            settings.EMAIL_DELIVERABILITY_USER, settings.EMAIL_DELIVERABILITY_PASSWORD
        ) as mailbox:
            for msg in mailbox.fetch(AND(subject=f"{subject}")):
                logger.debug(f"Message {msg.uid} {msg.date} {msg.subject} found in mailbox")
                mailbox.delete(msg.uid)
                return HttpResponse("OK", status=200)

    return HttpResponse("KO", status=400)
