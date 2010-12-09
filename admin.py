from django.contrib import admin

from nest_bizplan.models import Entry

class EntryAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'applicant', 'email', 'city', 'state', 'country', 'is_startl_applicant', ]


admin.site.register(Entry, EntryAdmin)