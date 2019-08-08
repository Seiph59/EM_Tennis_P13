from django import forms
from events.models import Registration

class RegistrationForm(forms.ModelForm):
    """ Forms for the registration informations
    added or modified by the user """
    registered = forms.BooleanField(label="Valider son inscription")
    adult_number = forms.IntegerField(label="Nombre d'adulte(s)")
    child_number = forms.IntegerField(label="Nombre d'enfant(s)")

    class Meta:
        """Define the order of fields"""
        model = Registration
        fields = ('adult_number', 'child_number', 'registered')



