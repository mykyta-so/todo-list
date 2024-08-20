from datetime import date
from django import forms
from todo.models import Task, Tag


class TaskForm(forms.ModelForm):
    tags = forms.ModelMultipleChoiceField(
        queryset=Tag.objects.all(),
        widget=forms.CheckboxSelectMultiple(),
        required=False,
    )
    deadline = forms.DateTimeField(
        widget=forms.DateTimeInput(attrs={"class": "datepicker"}),
        initial=date.today(),
        required=False,
    )

    class Meta:
        model = Task
        fields = (
            "content",
            "deadline",
            "done",
            "tags",
        )


class TagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = "__all__"
