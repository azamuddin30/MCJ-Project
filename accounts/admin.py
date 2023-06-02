from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import UserCreationForm, UserEditForm, TeamRegisterForm
from .models import User, Team


# Register your models here.
class CustomUserAdmin(UserAdmin):
    add_form = UserCreationForm
    form = UserEditForm
    model = User
    list_display = [  
        "username",
        "email",
        "is_staff",
        "is_superuser",
    ]
    fieldsets = UserAdmin.fieldsets + (
        ('Team', {'fields': ('team',)}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        ('Team', {'fields': ('team',)}),
    )


class TeamAdmin(admin.ModelAdmin):
    list_display = ("name", "description")


admin.site.register(User, CustomUserAdmin)
admin.site.register(Team, TeamAdmin)
