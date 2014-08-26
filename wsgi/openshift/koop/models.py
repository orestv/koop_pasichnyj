from django.db import models

# Create your models here.
import django.db.models as django_models


class Upload(models.Model):
    filename = django_models.CharField(max_length=512)
    file = django_models.FileField(verbose_name=u'Звіт', upload_to='uploads')