from django.db import models
from multilingual_model.models import MultilingualModel, MultilingualTranslation


class Entry(MultilingualModel):
    sname = models.SlugField(primary_key=True)

    def __str__(self):
        return self.sname


class EntryTranslation(MultilingualTranslation):
    class Meta:
        unique_together = ('parent', 'language_code')

    parent = models.ForeignKey(Entry, related_name='translations')
    header = models.CharField(max_length=200)
    text = models.TextField()