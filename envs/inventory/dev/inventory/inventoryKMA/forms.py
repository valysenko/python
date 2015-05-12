__author__ = 'vladyslav'
from .models import Task, Classroom, UnitItem
from django.forms import ModelForm

class TaskForm(ModelForm):
    class Meta:
        model = Task
        exclude = ['id']

class ClassroomForm(ModelForm):
    class Meta:
        model = Classroom
        exclude = ['id']

class UnitItemForm(ModelForm):
    class Meta:
        model = UnitItem
        exclude = ('id','workplace','unit')