from django.db import models

class Protein(models.Model):
    MAX_LENGTH = 1200
    sequence = models.CharField(max_length=MAX_LENGTH)
    # If null is True then label can be None
    label = models.CharField(max_length=MAX_LENGTH, null=True)

    def __str__(self):
        return self.sequence
