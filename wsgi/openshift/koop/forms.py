from crispy_forms.bootstrap import FormActions
from crispy_forms.helper import FormHelper
import crispy_forms.layout as crispy_layout
import django.forms as django_forms
import koop.models as koop_models


class UploadForm(django_forms.ModelForm):
    class Meta:
        model = koop_models.Report
        fields = (
            'file',
            'folder',
        )

    def __init__(self, *args, **kwargs):
        super(UploadForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'fileUploadForm'
        self.helper.form_action = 'upload'
        self.helper.layout = crispy_layout.Layout(
            'file',
            crispy_layout.Field('folder', type='hidden', id='fileUploadFolderId'),
            # crispy_layout.Hidden('folder', None, id='fileUploadFolderId'),
            FormActions(
                crispy_layout.Submit('upload',
                                     'Завантажити',
                                     css_class='btn btn-large',
                                     data_loading_text='Завантаження...'),
            ),
        )

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
            'parent',
        )

    def __init__(self, *args, **kwargs):
        super(FolderForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = crispy_layout.Layout(
            crispy_layout.Field('name', value='', autofocus=True),
            crispy_layout.Field('parent', type='hidden'),
        )