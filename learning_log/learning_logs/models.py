"""Define the data we want to manage in our app."""
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

# A model tells Django how to work with data that will be stored in the app.


class Topic(models.Model):
    """A topic that user is learning about."""

    text = models.CharField(max_length=200)  # topic name
    date_added = models.DateTimeField(auto_now_add=True)
    # (auto_now_add=True) -> sets to current date and time whenever the user creates a new topic
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    # we add owner field to Topic, which establishes a foreign key relationship to the User model
    # If a user is deleted, all the topics associated with that user will be deleted as well.

    def __str__(self):
        """Return the string respresentation of the model."""
        return str(self.text)


class Entry(models.Model):
    """Something specific learned about a topic."""

    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "entries"

    def __str__(self):
        """Return a string representation of a model."""
        if len(self.text) > 50:
            return f"{self.text[:50]}..."
        return f"{self.text}"
