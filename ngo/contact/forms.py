from contact.models import feedback
from django import forms

class gform(forms.ModelForm):

    class Meta():
        model=feedback
        fields=('email','message',)

        widgets={ 'message': forms.Textarea(attrs={'class': 'form-control editable medium-editor-textarea postcontent','style': 'background-color:rgba(0, 0, 0, 0); '}), 'email': forms.TextInput(attrs={'class': 'form-control editable medium-editor-textarea postcontent','style': 'background-color:rgba(0, 0, 0, 0); '})}
