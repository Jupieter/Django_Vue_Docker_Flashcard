from django import forms
from .models import Card

class CardCheckForm(forms.Form):
    card_id = forms.IntegerField(required=True)
    solved = forms.BooleanField(required=False)

class ChangeSetForm(forms.ModelForm):
    """  Hier may set the Card-set """
    class Meta:
        model = Card
        fields = ('card_set', )