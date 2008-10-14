from django import forms
from models import CategoryImage
from scofield.core.widgets import AdminImageWidget

class FileUploadForm(forms.ModelForm):
    picture = forms.FileField(widget=AdminImageWidget)

    class Meta:
        model = CategoryImage

