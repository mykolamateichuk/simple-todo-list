from django import forms

from todo_list.models import Tag, Task


class TagCreateForm(forms.ModelForm):

    class Meta:
        model = Tag
        fields = ("name", )


class DateInput(forms.DateInput):
    input_type = "date"


class TaskCreateForm(forms.ModelForm):
    tags = forms.ModelMultipleChoiceField(
        queryset=Tag.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=True
    )

    class Meta:
        model = Task
        fields = "__all__"
        widgets = {
            "deadline": DateInput()
        }
