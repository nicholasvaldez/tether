from django.db import models


class TouchType(models.Model):
    type_name = models.CharField(max_length=155)
    description = models.TextField(blank=True, null=True)
