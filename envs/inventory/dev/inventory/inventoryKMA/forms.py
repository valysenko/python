__author__ = 'vladyslav'
from django import forms
from .models import Task, Classroom, UnitItem,Complaint
from django.forms import ModelForm
from django.contrib.auth.models import User, Permission
from django.db.models import Q


class TaskForm(ModelForm):
    class Meta:
        model = Task
        exclude = ['id','status']
    message = forms.CharField(widget=forms.Textarea)
    perm = Permission.objects.get(codename='delete_task')
    assistant = forms.ModelChoiceField(queryset=User.objects.filter(Q(groups__permissions=perm) | Q(user_permissions=perm) ).distinct())


class ClassroomForm(ModelForm):
    class Meta:
        model = Classroom
        fields = ['columns','rows','number']
        exclude = ['id']
    perm = Permission.objects.get(codename='delete_task')
    assistant = forms.ModelChoiceField(queryset=User.objects.filter(Q(groups__permissions=perm) | Q(user_permissions=perm) ).distinct())


class UnitItemForm(ModelForm):
    class Meta:
        model = UnitItem
        exclude = ('id','workplace','unit')

class UnmanagedClassroomForm(ModelForm):
    class Meta:
        model = Classroom
        exclude = ['id', 'columns', 'rows', 'number']
    perm = Permission.objects.get(codename='delete_task')
    assistant = forms.ModelChoiceField(queryset=User.objects.filter(Q(groups__permissions=perm) | Q(user_permissions=perm) ).distinct())

class UnmanagedTaskForm(ModelForm):
    class Meta:
        model = Task
        exclude = ['id', 'status', 'message']
    perm = Permission.objects.get(codename='delete_task')
    assistant = forms.ModelChoiceField(queryset=User.objects.filter(Q(groups__permissions=perm) | Q(user_permissions=perm) ).distinct())

class ComplaintForm(ModelForm):
    class Meta:
        model = Complaint
        exclude = ['id', 'workplace']
    message = forms.CharField(widget=forms.Textarea)