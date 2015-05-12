from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.views.generic import FormView
from .forms import TaskForm, ClassroomForm, UnitItemForm
from .models import  Workplace, Classroom, Unit,UnitItem
from django.contrib.auth.models import User, Permission
from django.db.models import Q
import traceback
# Create your views here.

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

        perm = Permission.objects.get(codename='blogger')
        users = User.objects.filter(Q(groups__permissions=perm) | Q(user_permissions=perm) ).distinct()

        form = self.form_class()
        context = self.get_context_data(**kwargs)
        context['form'] = form
        return self.render_to_response(context)
    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            task = form.save()
            # <process form cleaned data>
            return redirect('/')
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
            return redirect('/')
        return render(request, self.template_name, {'form': form})

