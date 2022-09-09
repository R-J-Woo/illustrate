from django.contrib import admin
<<<<<<< HEAD
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from .models import Profile


# Register your models here.
=======
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import Profile

# Register your models here.


>>>>>>> e9ae3b523566da25597a16b68da2b86a584fd8e0
class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False
    verbose_name_plural = 'profile'


class UserAdmin(BaseUserAdmin):
<<<<<<< HEAD
    inlines = (ProfileInline, )
=======
    inlines = (ProfileInline,)
>>>>>>> e9ae3b523566da25597a16b68da2b86a584fd8e0


admin.site.unregister(User)
admin.site.register(User, UserAdmin)
