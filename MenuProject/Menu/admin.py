from django.contrib import admin
from django.contrib.admin import actions

from .models import *


# Register your models here.

class InlineModelMenu(admin.StackedInline):
    model = ModelMenu
    extra = 1
    fk_name = 'parent'


class FriendshipInline(admin.TabularInline):
    model = ModelMenu
    extra = 1
    fk_name = 'another_menu'


class ModelMenuAdmin(admin.ModelAdmin):
    model = ModelMenu
    inlines = [InlineModelMenu]
    list_display = ('name', 'id')


admin.site.register(ModelMenu, ModelMenuAdmin)
