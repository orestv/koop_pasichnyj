from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Hidden
import django.forms as django_forms
import koop.models as koop_models


class UploadForm(django_forms.ModelForm):
    class Meta:
        model = koop_models.Report
        fields = (
            'file',
        )

    def __init__(self, *args, **kwargs):
        super(UploadForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.add_input(Submit('upload', 'Upload', css_class='btn btn-large'))

    def save(self, commit=True):
        upload = super(UploadForm, self).save(commit=False)
        upload.filename = upload.file.name
        upload.save()
        return upload


class FolderForm(django_forms.ModelForm):
    class Meta:
        model = koop_models.Folder
        fields = (
            'name',
            # 'parent',
        )

    def __init__(self, *args, **kwargs):
        super(FolderForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            'name',
            Submit('save', 'Зберегти'),
        )