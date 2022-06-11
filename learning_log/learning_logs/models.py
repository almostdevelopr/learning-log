"""Define the data we want to manage in our app."""
from django.db import models

# Create your models here.

# A model tells Django how to work with data that will be stored in the app.


class Topic(models.Model):
    """A topic that user is learning about."""

    text = models.CharField(max_length=200)  # topic name
    date_added = models.DateTimeField(auto_now_add=True)
    # (auto_now_add=True) -> sets to current date and time whenever the user creates a new topic

    def __str__(self):
        """Return the string respresentation of the model."""
        return str(self.text)
