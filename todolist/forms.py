from django import forms

class TaskForm(forms.Form):
    title = forms.CharField(label= "Title", max_length=200)
    description = forms.CharField(label= "Description", max_length=500)