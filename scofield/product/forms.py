from django import forms
from scofield.core.forms import ImageUploadForm
from models import *

class ProductImageForm(ImageUploadForm):
    
    class Meta:
        model = ProductImage
