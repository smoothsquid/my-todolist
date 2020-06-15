from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_list_or_404, get_object_or_404
from task.forms import SimpleTaskForm
from task.models import Task, get_max_order_num
from django.utils.translation import ugettext_lazy as _

@login_required
def index(request):
    form = SimpleTaskForm()
    # TODO: 순서를 정하고 정렬하여 보여줘야함
    tasks = Task.objects.all()
    return render(request, 'task/index.html', {'title': _('Welcome'), 'form': form, 'tasks': tasks, })

@login_required
def add(request):
    if request.method == "POST":
        form = SimpleTaskForm(request.POST)
        if form.is_valid:
            task = form.save(commit=False)
            task.author = request.user
            task.order_num = get_max_order_num(request.user) + 1
            task.save()
        return redirect('task:index')
    else:
        pass
    return None

@login_required
def done(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.is_done = True
    task.save()
    return redirect('task:index')

@login_required
def delete(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.delete()
    return redirect('task:index')

@login_required
def incomplete(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.is_done = False
    task.save()
    return redirect('task:index')

@login_required
def re_order(request, pk, order):
    task = get_object_or_404(Task, pk=pk)
    if order is task.order_num:
        return

    origin_order = task.order
    new_order = order
    task.order_num = new_order

    tasks = get_list_or_404(Task, filter(order__gt=origin_order, order__lte=new_order))

    new_order_is_great = new_order > origin_order

    for item in tasks:
        if new_order_is_great:
            item.order_num = item.order_num - 1
        else:
            item.order_num = item.order_num + 1
        
    return
