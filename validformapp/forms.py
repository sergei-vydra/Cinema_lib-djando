from django import forms
from django.core import validators


def validate_name(name):
    if not name.startswith("a"):
        raise forms.ValidationError("Name must start with 'a' letter!")


class NameForm(forms.Form):
    name = forms.CharField(validators=[validate_name])
    email = forms.CharField()
    vmail = forms.CharField()
    text = forms.CharField(widget=forms.Textarea, validators=[validators.MaxLengthValidator(5)])

    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data["email"]
        vmail = cleaned_data["vmail"]
        if email != vmail:
            raise forms.ValidationError("Email and Vmail fields must be the same!")
