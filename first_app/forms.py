from django import forms
from first_app.models import User

# if you want to connect to a model you need ModelForm
class NewUserForm(forms.ModelForm):
    # custom validations here
    # name = forms.CharField(validator ..)
    class Meta():
        model = User
        fields = '__all__'
