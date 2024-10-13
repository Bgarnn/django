from django import forms

class InputForm(forms.Form):
    text = forms.CharField(label='Your Input', max_length=100)
