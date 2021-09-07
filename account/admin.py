from django.contrib import admin

from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from account.models import User


class CustomUserCreationForm(UserCreationForm):
    readonly_fields = ["date_joined"]

    class Meta(UserCreationForm):
        model = User
        fields = ('username', 'email')


class CustomUserChangeForm(UserChangeForm):
    readonly_fields = ["date_joined"]

    class Meta:
        model = User
        fields = ('username',)


class CustomUserAdmin(UserAdmin):
    readonly_fields = ["date_joined"]
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = User
    list_display = ['phone', 'first_name', 'last_name', 'email', 'username']


admin.site.register(User, CustomUserAdmin)
