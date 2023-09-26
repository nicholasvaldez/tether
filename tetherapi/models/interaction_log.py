from django.db import models


class InteractionLog(models.Model):

    TEXT_MESSAGE = 'text_message'
    PHONE_CALL = 'phone_call'
    MEETUP = 'meetup'
    EMAIL = 'email'
    OTHER = 'other'

    INTERACTION_TYPES = [
        (TEXT_MESSAGE, 'Text Message'),
        (PHONE_CALL, 'Phone Call'),
        (MEETUP, 'Meetup'),
        (EMAIL, 'Email'),
        (OTHER, 'Other'),
    ]

    contact = models.ForeignKey(
        "Contact", on_delete=models.CASCADE, related_name='interactions')
    interaction_type = models.CharField(
        max_length=20,
        choices=INTERACTION_TYPES,
        default=TEXT_MESSAGE,
    )
    date = models.DateField()
    notes = models.TextField(blank=True, null=True)
