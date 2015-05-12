__author__ = 'vladyslav'

from django.conf.urls import patterns, include, url
from .views import TaskView, ClassroomView, UnitItemView

urlpatterns = [
    url(r'^task/add$', TaskView.as_view(), name='add_task'),
    url(r'^classroom/add$', ClassroomView.as_view(), name='add_classroom'),
    url(r'^classrooms/list$', 'inventoryKMA.views.classrooms_list', name='classrooms_list'),
    url(r'^classroom/(?P<number>\d+)/$', 'inventoryKMA.views.classroom_show', name='classroom_show'),
    url(r'^unit_item/new/(?P<id>\d+)/$', UnitItemView.as_view(), name='unit_item_new'),
    url(r'^unit_item/delete/(?P<id>\d+)/$', 'inventoryKMA.views.delete_unit_item', name='delete_unit_item'),
]