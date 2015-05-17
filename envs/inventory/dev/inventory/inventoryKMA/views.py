from django.shortcuts import render, redirect, get_object_or_404
import json
from django.http import HttpResponse,JsonResponse
from django.views.generic import FormView
from .forms import TaskForm, ClassroomForm, UnitItemForm, UnmanagedClassroomForm, UnmanagedTaskForm, ComplaintForm
from .models import  Workplace, Classroom, Unit, UnitItem, Task, Complaint
from django.contrib.auth.models import User, Permission, Group
from django.db.models import Q
from django.core.mail import send_mail
from django.contrib.auth.decorators import login_required
from django.core import serializers

"""
For email sending
"""
def get_admin_email():
    perm = Permission.objects.get(codename='add_classroom')
    user=User.objects.get(groups__permissions=perm)
    return user.email

email_from = 'inventorykma@gmail.com'
complaint_subject = 'A new complaint'
task_subject = 'A new task for you'
admin_email = get_admin_email()


"""
Views for admin
"""
def create_assistant(request,id):
    assistant = User.objects.get(pk=id)
    assistant_group, created = Group.objects.get_or_create(name='assistant')
    user_group, created1 = Group.objects.get_or_create(name='user')
    user_group.user_set.remove(assistant)
    assistant.groups.add(assistant_group)
    return redirect('/assistants/list')

@login_required
def find_user(request):
    return render(request, "find_user.html")

@login_required
def get_users(request,email):
    users=User.objects.filter(email__startswith=email).distinct()
    object_dict = dict((x.id, x.first_name+" "+x.last_name+" ("+x.email+")") for x in users)

    return JsonResponse(object_dict)

@login_required
def complaints_list(request):
    complaints = Complaint.objects.all()
    return render(request, "complaints_list.html", {'complaints':complaints})

@login_required
def complaints_workplace_list(request,id):
    workplace = Workplace.objects.get(pk=id)
    complaints = workplace.complaints.all
    return render(request, "complaints_list.html", {'complaints':complaints})

def delete_complaint(request,id):
    complaint = Complaint.objects.filter(pk=id).delete()
    return redirect('/redirect')

@login_required
def classrooms_list(request):
    classrooms = Classroom.objects.all()
    return render(request, "classrooms_list.html", {'classrooms':classrooms})

@login_required
def classroom_show(request, number):
    classroom = Classroom.objects.get(number=number)
    width = classroom.columns*(135+3)
    return render(request, "classroom_show.html", {'classroom':classroom, 'width':width})

@login_required
def delete_unit_item(request, id):
    unit_item = UnitItem.objects.filter(pk=id).delete()
    return HttpResponse('')


@login_required
def unmanage_classroom(request,id):
    classroom = Classroom.objects.get(pk=id)
    classroom.assistant = None
    classroom.save()
    return redirect('/classrooms/list')

@login_required
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


@login_required
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

@login_required
def unmanaged_classrooms_list(request):
    classrooms = Classroom.objects.filter(assistant=None)
    return render(request, "unmanaged_classrooms_list.html", {'classrooms':classrooms})

@login_required
def unmanaged_tasks_list(request):
    tasks = Task.objects.filter(assistant=None)
    return render(request, "unmanaged_tasks_list.html", {'tasks':tasks})

@login_required
def assistants_list(request):
    perm = Permission.objects.get(codename='delete_task')
    assistants = User.objects.filter(Q(groups__permissions=perm) | Q(user_permissions=perm) ).distinct()
    return render(request, "assistants_list.html", {'assistants':assistants})


@login_required
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
            send_mail(task_subject,
                      task.message,
                      email_from,
                    [task.assistant.email])
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

@login_required
def in_progress_tasks_list(request):
    tasks = Task.objects.filter(assistant=request.user,status="in progress")
    return render(request, "current_tasks_list.html", {'tasks':tasks})


@login_required
def finished_tasks_list(request):
    tasks = Task.objects.filter(assistant=request.user,status="finished").all()
    return render(request, "finished_tasks_list.html", {'tasks':tasks})


@login_required
def finish_task(request,id):
    task = Task.objects.get(pk=id)
    task.status = "finished"
    task.save()
    return redirect('/tasks/current')


"""
Views for user
"""
@login_required
def classrooms_for_user_list(request):
    classrooms = Classroom.objects.all()
    return render(request, "classrooms_for_user_list.html", {'classrooms':classrooms})


@login_required
def classroom_for_user_show(request, number):
    classroom = Classroom.objects.get(number=number)
    width = classroom.columns*(135+3)
    return render(request, "classroom_for_user_show.html", {'classroom':classroom, 'width':width})



class ComplaintView(FormView):
    form_class = ComplaintForm
    template_name = 'complaint.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        context = self.get_context_data(**kwargs)
        context['form'] = form
        context['w_id'] = kwargs["id"]
        return self.render_to_response(context)
    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            complaint = form.instance
            send_mail(complaint_subject,
                      complaint.message,
                      email_from,
                    [admin_email])
            complaint = form.instance
            workplace_id = request.POST["workplace_id"]
            workplace = Workplace.objects.get(pk=workplace_id)
            complaint.workplace = workplace
            complaint.save()
            return redirect('/redirect')
        return render(request, self.template_name, {'form': form,'w_id':kwargs["id"]})