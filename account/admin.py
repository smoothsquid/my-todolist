from django.contrib import admin
from .models import User
from .forms import UserCreationForm, UserChangeForm

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    change_form = UserChangeForm
    add_form = UserCreationForm

    list_display = ('id', 'email', 'date_of_birth', 'is_admin')
    list_filter = ('is_admin',)
    
    
    search_fields = ('username', 'email', 'name',)
    ordering = ('-id',)

    def get_form(self, request, obj=None, **kwargs):
        if not obj:
            self.form = self.add_form
            self.fieldsets = (
                (None, {
                    'fields': ('username', 'name', 'email', 'date_of_birth', 'password1', 'password2')}
                    ),
            )
        else:
            self.form = self.change_form
            self.fieldsets = (
                (None, {'fields': ('username', 'name', 'email', 'password')}),
                ('Personal info', {'fields': ('date_of_birth',)}),
                ('Permissions', {'fields': ('is_admin',)}),
            )

        return super(UserAdmin, self).get_form(request, obj, **kwargs)