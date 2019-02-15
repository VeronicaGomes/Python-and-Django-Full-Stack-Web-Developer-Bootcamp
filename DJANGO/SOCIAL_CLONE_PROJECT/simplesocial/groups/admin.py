from django.contrib import admin
from . import models

# Register your models here.

class GroupMemberInLine(admin.TabularInLine):
    model = models.GroupMember

admins.site.register(models.Group)
