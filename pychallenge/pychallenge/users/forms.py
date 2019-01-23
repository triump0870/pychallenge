from django import forms

from markdownx.fields import MarkdownxFormField

from pychallenge.users.models import About


class AboutForm(forms.ModelForm):
    status = forms.CharField(widget=forms.HiddenInput())
    content = MarkdownxFormField()

    class Meta:
        model = About
        fields = ["content", "status"]
