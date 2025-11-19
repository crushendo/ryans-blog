from django.contrib import admin
from blogapp.models import Summaries

# admin housekeeping
class SummariesAdmin(admin.ModelAdmin):
    model = Summarieslist_display = ('title', 'date')
    prepopulated_fields = {'slug': ('title',)}

# Register your models here.
admin.site.register(Summaries, SummariesAdmin)
