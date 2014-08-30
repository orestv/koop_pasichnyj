from django.db import models

# Create your models here.
import django.db.models as django_models


class Folder(models.Model):
    name = django_models.CharField(max_length=256, default='/')
    created_on = django_models.DateTimeField(auto_now_add=True)
    parent = django_models.ForeignKey('self',
                                      related_name='children',
                                      default=None,
                                      null=True)

    def __str__(self):
        return self.name


class Report(models.Model):
    filename = django_models.CharField(max_length=512)
    folder = django_models.ForeignKey(Folder,
                                      null=True,
                                      related_name='reports',
                                      default=None)
    file = django_models.FileField(verbose_name=u'Звіт',
                                   upload_to='uploads')

    def __str__(self):
        return self.filename