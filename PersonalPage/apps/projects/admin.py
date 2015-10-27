from django.contrib import admin
from sorl.thumbnail.admin import AdminImageMixin
from multilingual_model.admin import TranslationStackedInline
from projects.models import Project, Picture, Category, CategoryTranslation, ProjectTranslation


class CategoryInline(admin.TabularInline):
    model = Category


class ProjectTranslationInline(TranslationStackedInline):
    model = ProjectTranslation


class PictureInline(admin.TabularInline):
    model = Picture


class ProjectAdmin(AdminImageMixin, admin.ModelAdmin):
    model = Project
    list_display = ('sname', 'name', 'url')
    inlines = [ProjectTranslationInline, PictureInline]


class CategoryTranslationInline(TranslationStackedInline):
    model = CategoryTranslation


class CategoryAdmin(admin.ModelAdmin):
    model = Category
    inlines = [CategoryTranslationInline]

admin.site.register(Project, ProjectAdmin)
admin.site.register(Category, CategoryAdmin)
