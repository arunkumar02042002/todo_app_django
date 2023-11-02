from django.shortcuts import get_object_or_404, redirect, render, HttpResponse
from .models import Task

# Home View: Lists pending and completed tasks
def home(request):
    # Fetch pending tasks (not completed) and order them by the last update
    pending_tasks = Task.objects.filter(is_completed=False).order_by('-updated_at')
    
    # Fetch completed tasks and order them by the last update
    completed_tasks = Task.objects.filter(is_completed=True).order_by('-updated_at')
    
    context = {
        'pending_tasks': pending_tasks,
        'completed_tasks': completed_tasks,
    }
    return render(request, 'todos/home.html', context=context)

# Add Task View: Adds a new task to the list
def addTask(request):
    task = request.POST.get('task')
    
    # Create a new task with the specified content
    Task.objects.create(task=task)
    
    return redirect("/")

# Mark Task as Done View: Marks a task as completed
def markDone(request, pk):
    obj = get_object_or_404(Task, pk=pk)
    
    # Set the 'is_completed' field to True and save the task
    obj.is_completed = True
    obj.save()
    
    return redirect("/")

# Mark Task as Undone View: Marks a completed task as pending
def markUndone(request, pk):
    obj = get_object_or_404(Task, pk=pk)
    
    # Set the 'is_completed' field to False and save the task
    obj.is_completed = False
    obj.save()
    
    return redirect("/")

# Delete Task View: Deletes a task from the list
def deleteTask(request, pk):
    obj = get_object_or_404(Task, pk=pk)
    
    # Delete the task
    obj.delete()
    
    return redirect("/")

# Edit Task View: Allows editing the content of a task
def editTask(request, pk):
    obj = get_object_or_404(Task, pk=pk)
    
    if request.method == 'POST':
        # Update the task content based on the user's input and save the changes
        obj.task = request.POST.get('task')
        obj.save()
        
        return redirect('/')
    else:
        context = {
            'object': obj,
        }
        return render(request, 'todos/edit.html', context)