from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Task

@login_required
def task_list(request):
    tasks = Task.objects.filter(user=request.user)
    return render(request, 'todo/task_list.html', {'tasks': tasks})

@login_required
def add_task(request):
    if request.method == "POST":
        title = request.POST.get("title")
        Task.objects.create(user=request.user, title=title)
        return redirect('task_list')
    return redirect('task_list')

@login_required
def complete_task(request, id):
    task = Task.objects.get(id=id, user=request.user)
    task.is_completed = True
    task.save()
    return redirect('task_list')

@login_required
def delete_task(request, id):
    Task.objects.filter(id=id, user=request.user).delete()
    return redirect('task_list')
@login_required
def add_task(request):
    if request.method == "POST":
        title = request.POST.get("title")
        due_date = request.POST.get("due_date")
        due_time = request.POST.get("due_time")

        Task.objects.create(
            user=request.user,
            title=title,
            due_date=due_date if due_date else None,
            due_time=due_time if due_time else None,
        )

        return redirect('task_list')

