from django import forms
from widgets import AdminImageWidget

class ImageUploadForm(forms.ModelForm):
    image = forms.FileField(widget=AdminImageWidget)
