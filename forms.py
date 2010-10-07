from django import forms

from nest_bizplan.models import Entry

class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry