from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Permission, User, Group
# from var_dump import var_dump
# Create your views here.


def redirect_to_main(request):
    if request.user.groups.filter(name='admin').exists():
        return redirect('/classrooms/list')
    elif request.user.groups.filter(name='assistant').exists():
        return redirect('/assistant')
    elif request.user.groups.filter(name='user').exists():
        return redirect('/user')
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

    return render(request, "cabinet.html")


