from django import forms
from .models import book

class bookform(forms.ModelForm):

    class Meta:
        model = book
        fields = (
            "name",
            "publish_date",
            "isbn",
            "image",
            "publishing_house",
        )
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'publish_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'isbn': forms.TextInput(attrs={'class': 'form-control'}),
            'image': forms.FileInput(attrs={'class': 'form-control'}),
            'publishing_house': forms.Select(attrs={'class': 'form-control'}),
        }

