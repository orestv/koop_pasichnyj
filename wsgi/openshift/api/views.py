from django.shortcuts import render

# Create your views here.
from django.views.generic.base import View

from rest_framework.response import Response
from rest_framework.views import APIView

from koop import models as koop_models


class TreeView(APIView):
    def dump_folder(self, folder):
        data = {}
        if folder.parent:
            data['parent'] = str(folder.parent_id)
        else:
            data['parent'] = '#'
        data['id'] = folder.id
        data['text'] = folder.name
        data['type'] = 'folder'

        return data

    def dump_report(self, report):
        pass

    def get(self, *args, **kwargs):
        folder_list = map(self.dump_folder, koop_models.Folder.objects.all())
        # report_list = map(self.dump_report, koop_models.Report.objects.all())
        report_list = []

        data = list(folder_list) + list(report_list)

        return Response(data)