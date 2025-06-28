from django.forms import ModelForm
from .models import profile
from django import forms

class ProfileForm(ModelForm):
    class Meta:
        model = profile
        fields = ['username', 'bio', 'profile_picture']
        widgets = {
            'username': forms.TextInput(attrs={
                'class': 'w-full px-4 py-2 border border-amber-300 rounded-md bg-white focus:outline-none focus:ring-2 focus:ring-amber-400',
                'placeholder': 'Enter your username',
            }),
            'bio': forms.Textarea(attrs={
                'class': 'w-full resize-none px-4 py-2 border border-amber-300 rounded-md bg-white focus:outline-none focus:ring-2 focus:ring-amber-400',
                'placeholder': 'Tell us something about yourself...',
                'rows': 4,
            }),
            'profile_picture': forms.ClearableFileInput(attrs={
                'class': 'w-full border border-amber-300 rounded-md p-2 bg-white text-amber-800 '
                         'file:mr-4 file:py-2 file:px-4 file:rounded-md file:border-0 '
                         'file:text-sm file:font-semibold file:bg-amber-200 file:text-amber-900 hover:file:bg-amber-300',
            }),
        }
        # widgets = {
        #     'username': forms.TextInput(attrs={'class': 'form-control'}),
        #     'bio': forms.Textarea(attrs={'class': 'form-control'}),
        #     'profile_picture': forms.ClearableFileInput(attrs={'class': 'form-control-file'}),
        # }