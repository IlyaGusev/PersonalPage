from django.db import models


class Game(models.Model):
    sname = models.SlugField(primary_key=True)
    template_path = models.CharField(max_length=200)

    def __str__(self):
        return self.sname