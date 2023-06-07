from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.forms import Textarea
from .models import CustomUser, Follow


class UserAdminConfig(UserAdmin):
    ordering = ('-join_date', )
    list_display = ('email', 'username', 'is_active', 'is_staff')
    search_fields = ('email', 'username', 'firstname', 'lastname')
    list_filter = ('email', 'username', 'firstname',
                   'lastname', 'is_staff', 'is_active')

    fieldsets = (
        (None, {'fields': ('email', 'username', 'firstname', 'lastname', 'picture', 'background_picture')}),
        ('Permissions', {'fields': ('is_staff', 'is_active')}),
        ('Personal', {'fields': ('bio', )}),
    )

    formfield_overrides = {
        CustomUser.bio: {'widget': Textarea(attrs={'row': 10, 'cols': 40})}
    }

    add_fieldsets = (
        (None, {
            'classes': ('wide', ),
            'fields': ('email', 'username', 'firstname', 'lastname', 'bio', 'password1', 'password2', 'is_active', 'is_staff')
        }),
    )


admin.site.register(CustomUser, UserAdminConfig)
admin.site.register(Follow)
