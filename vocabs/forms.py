from django import forms
from .models import Dictionary

# creating a form
class DictionaryForm(forms.ModelForm):

    # create meta class
    class Meta:
        # specify model to be used
        model = Dictionary

        # specify fields to be used
        fields = [
            "english",
            "hindi",
            "notes",
            "source",
        ]


