from django.contrib import admin
from .models import Waitlist


class WaitlistAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email',
                    'created_at', 'updated_at')
    search_fields = ('first_name', 'last_name')


admin.site.register(Waitlist, WaitlistAdmin)
