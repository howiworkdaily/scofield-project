from django import forms
from scofield.core.forms import ImageUploadForm
from models import * 

class CategoryImageForm(ImageUploadForm):
    
    class Meta:
        model = CategoryImage
