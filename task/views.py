from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from task.forms import SimpleTaskForm
from task.models import Task

@login_required
def index(request):
    form = SimpleTaskForm()
    # TODO: 순서를 정하고 정렬하여 보여줘야함
    tasks = Task.objects.all()
    return render(request, 'task/index.html', {'title': '안녕하세요', 'form': form, 'tasks': tasks, })

@login_required
def add(request):
    if request.method == "POST":
        form = SimpleTaskForm(request.POST)
        if form.is_valid:
            task = form.save(commit=False)
            task.author = request.user
            task.save()
        return redirect('task.index')
    else:
        pass
    return None

@login_required
def done(request):
    pass