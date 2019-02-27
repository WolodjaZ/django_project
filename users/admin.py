from django.contrib import admin
from .models import UserProfile
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .forms import RegistrationForm, EditProfileForm
from django.contrib.auth.models import User



class UserProFileInline(admin.StackedInline):
	model = UserProfile
	can_delete = False
	form = EditProfileForm
	add_form = RegistrationForm
	varbose_name_plural = 'user_profiles'
	fields = ('user', 'student_email')

class UserAdmin(BaseUserAdmin):
	inlines = (UserProFileInline,)
	form = EditProfileForm
	add_form = RegistrationForm
	list_display = ('username','first_name', 'last_name', 'email')
	#change_form_template
	fieldsets = (
        (None, {
            'fields': ('username', 'first_name', 'last_name', 'email')
        }),
    )

    #def get_queryset(self, request):
    #	gs = super().get_queryset(request)
    #	gs = gs.order_by('-first_name', '-last_name')
    #	return gs





admin.site.unregister(User)
admin.site.register(User, UserAdmin)