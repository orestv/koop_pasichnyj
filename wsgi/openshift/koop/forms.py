from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
import django.forms as django_forms
import koop.models as koop_models


class UploadForm(django_forms.ModelForm):
    class Meta:
        model = koop_models.Upload
        fields = (
            'file',
        )

    def __init__(self, *args, **kwargs):
        super(UploadForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.add_input(Submit('upload', 'Upload', css_class='btn btn-large'))