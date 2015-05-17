from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Permission, User, Group
from django.views.generic import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.core.urlresolvers import reverse_lazy


class SignUpView(CreateView):
    form_class = UserCreationForm
    template_name = "signup.html"
    success_url = reverse_lazy('index')



def redirect_to_main(request):
    # assistant_group, created = Group.objects.get_or_create(name='user')
    # user = User.objects.create_user(first_name="Igor",last_name="Igorev",email="",username="igor")
    # user.set_password("1")
    # user.groups.add(assistant_group)
    # user.save()
    if request.user.groups.filter(name='admin').exists():
        return redirect('/classrooms/list')
    elif request.user.groups.filter(name='assistant').exists():
        return redirect('/tasks/current')
    elif request.user.groups.filter(name='user').exists():
        return redirect('/classrooms/user/list')
    return redirect('/')



def create_groups(request):
    """
    Admin group
    """
    admin_group, created = Group.objects.get_or_create(name='admin')

    permission = Permission.objects.get(codename='add_classroom')
    admin_group.permissions.add(permission)
    permission = Permission.objects.get(codename='change_classroom')
    admin_group.permissions.add(permission)
    permission = Permission.objects.get(codename='delete_classroom')
    admin_group.permissions.add(permission)

    permission = Permission.objects.get(codename='add_workplace')
    admin_group.permissions.add(permission)

    permission = Permission.objects.get(codename='add_unititem')
    admin_group.permissions.add(permission)
    permission = Permission.objects.get(codename='delete_unititem')
    admin_group.permissions.add(permission)

    permission = Permission.objects.get(codename='add_task')
    admin_group.permissions.add(permission)

    # admin_group.user_set.add(request.user)
    """
    Assistant group
    """
    assistant_group, created = Group.objects.get_or_create(name='assistant')

    permission = Permission.objects.get(codename='delete_task')
    assistant_group.permissions.add(permission)

    """
    User group
    """
    user_group, created = Group.objects.get_or_create(name='user')

    permission = Permission.objects.get(codename='add_complaint')
    user_group.permissions.add(permission)

    """
    User creation
    """
    # assistant_group, created = Group.objects.get_or_create(name='assistant')
    # user = User.objects.create_user(first_name="Vlad",last_name="Lysenko",email="stalkervlad2011@ukr.net",username="vlad")
    # user.set_password("1")
    # user.groups.add(assistant_group)
    # user.save()
    return render(request, "cabinet.html")


