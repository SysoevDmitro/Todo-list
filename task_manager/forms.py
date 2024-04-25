from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError

from .models import Task, Tag


class TaskForm(forms.ModelForm):

    class Meta:
        model = Task
        fields = "__all__"


class TagForm(forms.ModelForm):

    class Meta:
        model = Tag
        fields = "__all__"
