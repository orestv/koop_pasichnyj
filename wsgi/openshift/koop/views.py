from django.shortcuts import render

# Create your views here.
from django.views.generic.edit import FormView, CreateView

import koop.forms as koop_forms


class UploadView(CreateView):
    form_class = koop_forms.UploadForm
    template_name = 'koop/main.html'
    success_url = '/'