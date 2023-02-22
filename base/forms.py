from asyncio.windows_events import NULL
from cProfile import label
from contextlib import nullcontext
from dataclasses import field
from email.policy import default
from unicodedata import name
from django import forms
from django.forms import EmailInput, ModelForm, TextInput,NumberInput
from .models import Deptartments, Student
from django.utils.translation import gettext_lazy as _

class StudentForm(ModelForm):
    required_css_class = 'update'
    GPA = forms.CharField(max_length=10,widget=forms.TextInput(attrs={'class': 'update'}),label='GPA')
    phone_Num = forms.CharField(widget=forms.TextInput(attrs={'class': 'update'}))
    class Meta:
        model = Student
        fields = ('name','ID','GPA','dob','level','gender','email','status','department','phone_Num')
        labels = {
            'name': _('Name'),
            'dob' : _('Date Of Birth'),
            'phone_Num': _('Phone Number'),
            'email': _('E-mail'),
        }
        widgets = {
            'dob': TextInput(attrs={'placeholder': 'yyyy-mm-dd'}),
            'email': EmailInput(attrs={'placeholder':'adel@example.com'}),
            'level': NumberInput(attrs={'step': '1', 'min': '1', 'max': '4'}),
        }

