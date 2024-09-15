from django import forms
from django.shortcuts import render

task = ["foo", "bar", "baz"]

class NewTasksForm(forms.Form):
    task = forms.CharField(label="New Task")
    priority = forms.IntegerField(label="Priority",min_value=1, max_value=10)
    
# Create your views here.
def index(request):
    return render (request,"tasks/index.html", {
        "task": task
    })
    
def add(request):
    return render(request, "tasks/add.html", {
        "form": NewTasksForm()
    })