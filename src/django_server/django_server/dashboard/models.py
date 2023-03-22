from django.db import models

class Protein(models.Model):
    MAX_LENGTH = 5000
    sequence = models.CharField(max_length=MAX_LENGTH)
    sequence_id = models.CharField(max_length=100)
    # If null is True then label can be None
    label = models.CharField(max_length=MAX_LENGTH, null=True)

    def __str__(self):
        return self.sequence
