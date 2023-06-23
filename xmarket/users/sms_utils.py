from twilio.rest import Client
from django.conf import settings

from twilio.rest import Client


def send_verification_code(phone_number, verification_code):
    client = Client(settings.TWILIO_ACCOUNT_SID, settings.TWILIO_AUTH_TOKEN )

    message = client.messages.create(
        from_='+14067095496',
        body='NAZAR DODIK',
        to=phone_number
    )

    return message.sid

import random

def generate_verification_code():
    # Generate a random 6-digit verification code
    verification_code = ''.join(random.choices('0123456789', k=6))
    return verification_code