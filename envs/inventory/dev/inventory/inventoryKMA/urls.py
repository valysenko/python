__author__ = 'vladyslav'

from django.conf.urls import patterns, include, url
from .views import TaskView, ClassroomView, UnitItemView

urlpatterns = [
    #admin urls

    url(r'^task/add$', TaskView.as_view(), name='add_task'),
    url(r'^task/manage/(?P<id>\d+)/$', 'inventoryKMA.views.manage_task', name='manage_task'),
    url(r'^task/unmanaged/list$', 'inventoryKMA.views.unmanaged_tasks_list', name='unmanaged_tasks_list'),

    url(r'^classroom/add$', ClassroomView.as_view(), name='add_classroom'),
    url(r'^classrooms/list$', 'inventoryKMA.views.classrooms_list', name='classrooms_list'),
    url(r'^classrooms/unmanaged/list$', 'inventoryKMA.views.unmanaged_classrooms_list', name='unmanaged_classrooms_list'),
    url(r'^classroom/unmanage/(?P<id>\d+)/$', 'inventoryKMA.views.unmanage_classroom', name='unmanage_classroom'),
    url(r'^classroom/manage/(?P<id>\d+)/$', 'inventoryKMA.views.manage_classroom', name='manage_classroom'),
    url(r'^classroom/(?P<number>\d+)/$', 'inventoryKMA.views.classroom_show', name='classroom_show'),

    url(r'^assistants/list$', 'inventoryKMA.views.assistants_list', name='assistants_list'),
    url(r'^assistant/delete/(?P<id>\d+)/$', 'inventoryKMA.views.delete_assistant', name='delete_assistant'),

    url(r'^unit_item/new/(?P<id>\d+)/$', UnitItemView.as_view(), name='unit_item_new'),
    url(r'^unit_item/delete/(?P<id>\d+)/$', 'inventoryKMA.views.delete_unit_item', name='delete_unit_item'),

    # assistant urls
    url(r'^tasks/current$', 'inventoryKMA.views.in_progress_tasks_list', name='current_tasks'),
    url(r'^tasks/finished$', 'inventoryKMA.views.finished_tasks_list', name='finished_tasks'),
    url(r'^task/finish/(?P<id>\d+)/$', 'inventoryKMA.views.finish_task', name='finish_task'),

]