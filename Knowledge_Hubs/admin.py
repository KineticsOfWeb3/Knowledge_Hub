from django.contrib import admin
from .models import Topic, Entry


class EntryAdmin(admin.ModelAdmin):
    list_display = ('topic', 'date_added', 'text')


class TopicAdmin(admin.ModelAdmin):
    list_display = ('text', 'date_added')


admin.site.register(Topic, TopicAdmin)
admin.site.register(Entry, EntryAdmin)

