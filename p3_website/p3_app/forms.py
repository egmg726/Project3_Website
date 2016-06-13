from django import forms

class RsForm(forms.Form):
    rs_id = forms.CharField(label='rsID:', max_length=100)
