from django.db import models
from django.core.validators import MinValueValidator, MinLengthValidator,MaxLengthValidator
from django.contrib.auth.models import User
# from ..user.models import InventoryUser

"""
    Managers for Entities
"""


class  ClassroomManager:
    pass


class  WorkplaceManager:
    pass


class  UnitManager:
    pass


class  UnitItemManager:
    pass


class  TaskManager:
    pass


class  ComplaintManager:
    pass




"""
    Entities
"""


class Classroom(models.Model):
    id=models.AutoField(primary_key=True)
    columns = models.IntegerField(validators=[MinValueValidator(0)])
    rows = models.IntegerField(validators=[MinValueValidator(0)])
    number = models.CharField(validators=[MinLengthValidator(0)], max_length=3)
    assistant = models.ForeignKey(User, related_name="classroom_assistant", null=True)
    objects = ClassroomManager()


class Workplace(models.Model):
    id=models.AutoField(primary_key=True)
    number = models.CharField(validators=[MinLengthValidator(0)], max_length=3)
    classroom = models.ForeignKey(Classroom)
    objects = WorkplaceManager()


class Unit(models.Model):
    id=models.AutoField(primary_key=True)
    name = models.CharField(max_length=15)
    objects = UnitManager()


class UnitItem(models.Model):
    id=models.AutoField(primary_key=True)
    number = models.CharField(validators=[MinLengthValidator(0)], max_length=15)
    workplace = models.ForeignKey(Workplace)
    unit = models.OneToOneField(Unit)
    objects = UnitItemManager()


class Task(models.Model):
    id=models.AutoField(primary_key=True)
    message = models.CharField(validators=[MinLengthValidator(0)], max_length=15)
    status = models.CharField(validators=[MinLengthValidator(0)], max_length=15)
    assistant = models.ForeignKey(User, related_name="tasks", null=True)
    objects = TaskManager()


class Complaint(models.Model):
    id=models.AutoField(primary_key=True)
    message = models.CharField(validators=[MinLengthValidator(0)], max_length=15)
    unit_item = models.ForeignKey(Workplace, related_name="complaints", null=True)
    objects = ComplaintManager()


