from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from .models import Task

@login_required
def dashboard(request):
    tasks = Task.objects.filter(user=request.user)
    total_tasks = tasks.count()
    unlocked_tasks = tasks.filter(is_unlocked=True).count()
    locked_tasks = total_tasks - unlocked_tasks

    context = {
        'tasks': tasks,
        'total_tasks': total_tasks,
        'unlocked_tasks': unlocked_tasks,
        'locked_tasks': locked_tasks
    }
    return render(request, 'course/dashboard.html', context)

@login_required
def unlock_task(request, task_id):
    task = get_object_or_404(Task, id=task_id, user=request.user)
    task.is_unlocked = True
    task.save()
    return redirect('dashboard')


def add_task(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        if title:
            Task.objects.create(user=request.user, title=title)
            return redirect('dashboard')
    return render(request, 'course/add_task.html')
