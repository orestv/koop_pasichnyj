from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView
from django.views.generic.edit import FormView, CreateView

import koop.forms as koop_forms
from koop.forms import FolderForm, UploadForm
from koop.models import Folder


class UploadView(CreateView):
    form_class = koop_forms.UploadForm
    template_name = 'koop/main.html'
    success_url = '/reports'


class MainView(TemplateView):
    template_name = 'koop/reports_base.html'

    def get_context_data(self, **kwargs):
        context = super(MainView, self).get_context_data(**kwargs)
        root_folder, created = Folder.objects.get_or_create(parent=None)
        context['root'] = root_folder

        folder_form = FolderForm()
        upload_form = UploadForm()

        context['folder_form'] = folder_form
        context['upload_form'] = upload_form

        return context