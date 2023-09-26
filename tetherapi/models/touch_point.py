from django.db import models
from django.contrib.auth.models import User


class TouchPoint(models.Model):

    contact = models.ForeignKey("Contact", on_delete=models.DO_NOTHING)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    touch_type = models.ForeignKey("TouchType", on_delete=models.DO_NOTHING)
    name = models.CharField(max_length=155)
    touch_date = models.DateField()
    notes = models.TextField(blank=True, null=True)
