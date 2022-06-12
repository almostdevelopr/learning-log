from django import forms

from .models import Topic, Entry


class TopicForm(forms.ModelForm):
    """A topic form in django style."""

    class Meta:
        model = Topic
        fields = ["text"]
        labels = {"text": ""}


class EntryForm(forms.ModelForm):
    """An entry for a specific topic."""

    class Meta:
        model = Entry
        fields = ["text"]
        labels = {"text": ""}
        widgets = {"text": forms.Textarea(attrs={"cols": 80})}
