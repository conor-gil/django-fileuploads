from django import forms
from . import models

class CreateFileUpload(forms.ModelForm):
    class Meta:
        model = models.FileUpload
        fields = ['description','file','slug','image']