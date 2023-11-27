from django import forms

from todo_list.models import Tag


class TagCreateForm(forms.ModelForm):

    class Meta:
        model = Tag
        fields = ("name", )
