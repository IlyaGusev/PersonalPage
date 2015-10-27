from django.contrib import admin
from entries.models import Entry, EntryTranslation
from multilingual_model.admin import TranslationStackedInline
# Register your models here.


class EntryTranslationInline(TranslationStackedInline):
   model = EntryTranslation


class EntryAdmin(admin.ModelAdmin):
    model = Entry
    list_display = ['sname']
    inlines = [EntryTranslationInline]

admin.site.register(Entry, EntryAdmin)