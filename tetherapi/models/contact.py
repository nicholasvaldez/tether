from django.db import models
from django.contrib.auth.models import User


class Contact(models.Model):

    ACQUAINTANCE = 'acquaintance'
    WARM = 'warm'
    CLOSE_FRIEND = 'close_friend'
    PERSONAL = 'personal'
    PROFESSIONAL = 'professional'

    CONTACT_TYPES = [
        (ACQUAINTANCE, 'Acquaintance'),
        (WARM, 'Warm'),
        (CLOSE_FRIEND, 'Close Friend'),
        (PERSONAL, 'Personal'),
        (PROFESSIONAL, 'Professional'),
    ]

    WEAK = 'weak'
    MODERATE = 'moderate'
    STRONG = 'strong'
    VERY_STRONG = 'very_strong'

    CONNECTION_STRENGTHS = [
        (WEAK, 'Weak'),
        (MODERATE, 'Moderate'),
        (STRONG, 'Strong'),
        (VERY_STRONG, 'Very Strong'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=155)
    contact_type = models.CharField(
        max_length=20,
        choices=CONTACT_TYPES,
        default=ACQUAINTANCE,
    )
    notes = models.TextField(blank=True, null=True)
    connection_strength = models.CharField(
        max_length=20,
        choices=CONNECTION_STRENGTHS,
        default=WEAK,
    )
