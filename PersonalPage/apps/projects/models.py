from django.db import models
from multilingual_model.models import MultilingualModel, MultilingualTranslation
from sorl.thumbnail import ImageField


class Category(MultilingualModel):
    sname = models.SlugField(primary_key=True)

    def __str__(self):
        return self.name


class CategoryTranslation(MultilingualTranslation):
    class Meta:
        unique_together = ('parent', 'language_code')

    parent = models.ForeignKey('Category', related_name='translations')
    name = models.CharField(max_length=200)


class Project(MultilingualModel):
    sname = models.SlugField(primary_key=True)
    name = models.CharField(max_length=200)
    date = models.DateField(blank=True)
    tech = models.CharField(max_length=200, blank=True)
    url = models.URLField(blank=True)
    zip = models.FileField(upload_to='files/', blank=True, null=True)
    categories = models.ManyToManyField(Category, related_name="projects")
    def __str__(self):
        return self.name


class Picture(models.Model):
    project = models.ForeignKey(Project, related_name="pictures")
    pic = ImageField(upload_to='images/', blank=True, null=True)


class ProjectTranslation(MultilingualTranslation):
    class Meta:
        unique_together = ('parent', 'language_code')

    parent = models.ForeignKey('Project', related_name='translations')
    description = models.TextField(blank=True)
    kind = models.CharField(max_length=200)
