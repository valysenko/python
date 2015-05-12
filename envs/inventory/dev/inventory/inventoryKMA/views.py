from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.views.generic import FormView
from .forms import TaskForm, ClassroomForm, UnitItemForm, UnmanagedClassroomForm, UnmanagedTaskForm
from .models import  Workplace, Classroom, Unit, UnitItem, Task
from django.contrib.auth.models import User, Permission, Group
from django.db.models import Q
import traceback

"""
Views for admin
"""

def classrooms_list(request):
    classrooms = Classroom.objects.all()
    return render(request, "classrooms_list.html", {'classrooms':classrooms})

def classroom_show(request, number):
    classroom = Classroom.objects.get(number=number)
    width = classroom.columns*(135+3)
    return render(request, "classroom_show.html", {'classroom':classroom, 'width':width})

def delete_unit_item(request, id):
    unit_item = UnitItem.objects.filter(pk=id).delete()
    return HttpResponse('')

def unmanage_classroom(request,id):
    classroom = Classroom.objects.get(pk=id)
    classroom.assistant = None
    classroom.save()
    return redirect('/classrooms/list')

def manage_classroom(request, id):
    classroom = get_object_or_404(Classroom, pk=id)
    if request.method == 'POST':
        form = UnmanagedClassroomForm(request.POST)
        if form.is_valid():
            assistant = form.instance.assistant
            classroom.assistant = assistant
            classroom.save()
            return redirect('/classrooms/list')
        else:
           return render(request, "manage_classroom.html", {'form': form})
    else:
        form = UnmanagedClassroomForm()
        return render(request, "manage_classroom.html", {'form': form})

def manage_task(request, id):
    task = get_object_or_404(Task, pk=id)
    if request.method == 'POST':
        form = UnmanagedTaskForm(request.POST)
        if form.is_valid():
            assistant = form.instance.assistant
            task.assistant = assistant
            task.save()
            return redirect('/task/unmanaged/list')
        else:
            return render(request, "manage_task.html", {'form': form})
    else:
        form = UnmanagedTaskForm()
        return render(request, "manage_task.html", {'form': form})


def unmanaged_classrooms_list(request):
    classrooms = Classroom.objects.filter(assistant=None)
    return render(request, "unmanaged_classrooms_list.html", {'classrooms':classrooms})

def unmanaged_tasks_list(request):
    tasks = Task.objects.filter(assistant=None)
    return render(request, "unmanaged_tasks_list.html", {'tasks':tasks})

def assistants_list(request):
    perm = Permission.objects.get(codename='delete_task')
    assistants = User.objects.filter(Q(groups__permissions=perm) | Q(user_permissions=perm) ).distinct()
    return render(request, "assistants_list.html", {'assistants':assistants})

def delete_assistant(request,id):
    assistant = User.objects.get(pk=id)
    assistant_group, created = Group.objects.get_or_create(name='assistant')
    user_group, created1 = Group.objects.get_or_create(name='user')
    assistant_group.user_set.remove(assistant)
    assistant.groups.add(user_group)
    tasks = Task.objects.filter(assistant=assistant)
    classrooms = Classroom.objects.filter(assistant=assistant)

    for task in tasks:
        task.assistant=None
        task.save()
    for classroom in classrooms:
        classroom.assistant=None
        classroom.save()

    assistant.save()
    return redirect('/assistants/list')

class UnitItemView(FormView):
    form_class = UnitItemForm
    # initial = {'key': 'value'}
    template_name = 'unit_item_new.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        context = self.get_context_data(**kwargs)
        context['form'] = form
        id = self.kwargs['id']
        workplace = Workplace.objects.get(pk=int(id))
        context['workplace'] = workplace
        return self.render_to_response(context)

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            unit_name = request.POST.get("type", "")
            unit = Unit.objects.get(name=unit_name)
            workplace_id = request.POST["workplace_id"]
            workplace = Workplace.objects.get(pk=workplace_id)
            unit_item = form.instance
            unit_item.unit = unit
            unit_item.workplace = workplace
            unit_item.save()
            classroom_number = request.POST["classroom_number"]
            return redirect('classroom_show', number=classroom_number)

        workplace_id = request.POST["workplace_id"]
        workplace = Workplace.objects.get(pk=workplace_id)
        return render(request, self.template_name, {'form': form,'workplace':workplace})

class TaskView(FormView):
    form_class = TaskForm
    # initial = {'key': 'value'}
    template_name = 'task.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        context = self.get_context_data(**kwargs)
        context['form'] = form
        return self.render_to_response(context)
    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            task = form.instance
            task.status="in progress"
            task.save()
            return redirect('/redirect')
        # return self.render_to_response(context)
        return render(request, self.template_name, {'form': form})


class ClassroomView(FormView):
    form_class = ClassroomForm
    # initial = {'key': 'value'}
    template_name = 'classroom.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        context = self.get_context_data(**kwargs)
        context['form'] = form
        return self.render_to_response(context)
    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            classroom = form.save()
            for x in range(0, classroom.columns*classroom.rows):
                classroom.workplace_set.add(Workplace(number=x+1))
            classroom.save()
            return redirect('/redirect')
        return render(request, self.template_name, {'form': form})

"""
Views for assistant
"""

def in_progress_tasks_list(request):
    tasks = Task.objects.filter(assistant=request.user,status="in progress")
    return render(request, "current_tasks_list.html", {'tasks':tasks})

def finished_tasks_list(request):
    tasks = Task.objects.filter(assistant=request.user,status="finished").all()
    return render(request, "finished_tasks_list.html", {'tasks':tasks})

def finish_task(request,id):
    task = Task.objects.get(pk=id)
    task.status = "finished"
    task.save()
    return redirect('/tasks/current')