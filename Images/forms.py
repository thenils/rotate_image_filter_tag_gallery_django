from django import forms
from .models import Tag


class FormTag(forms.Form):
    tags = Tag.objects.all()

    list = []
    for tag in tags:
        list.append(tuple((f'{tag}', f'{tag}')))

    OPTIONS = tuple(list)

    tag = forms.MultipleChoiceField(
        widget=forms.CheckboxSelectMultiple, choices=OPTIONS)
