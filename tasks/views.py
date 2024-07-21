from django import forms
from django.shortcuts import render,HttpResponseRedirect
from django.http import HttpResponseRedirect
from django.urls import reverse
# Cant import from here as well from django.shortcuts import render,HttpResponseRedirect




def index(request):
    if 'tasks' not in request.session:
        request.session['tasks']=[]

    return render(request,'tasks/index.html',{
        "tasks":request.session['tasks']
    })

def add(request):
    if request.method == "POST":
        form = NewTaskForm(request.POST)
        if form.is_valid():
            task = form.cleaned_data["tasks"]
            # tasks.append(task)
            request.session['tasks']+=[task]
            return HttpResponseRedirect(reverse('tasks:index'))
        else:
            return render(request,'tasks/add.html',{
                'form':form,
            })

    return render(request,'tasks/add.html',{
        'form':NewTaskForm(),
    })


class NewTaskForm(forms.Form):
    tasks = forms.CharField(label="Enter a Task")
    priority = forms.IntegerField(label="Priority",min_value=1, max_value=100)


