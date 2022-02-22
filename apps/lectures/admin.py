from django.contrib import admin
from .models import Lecture


class LectureAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'lecture_name', 'date',
                    'slides_url', 'created_at', 'updated_at')
    search_fields = ('title',)


admin.site.register(Lecture, LectureAdmin)
