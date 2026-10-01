from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.

from .models import Task



def task_list(request):
    #fetch all tasks from the database
    tasks = Task.objects.all().order_by("-created_at")

    #handle form submission to create a new task
    if request.method == "POST":
        title = request.POST.get("title")
        if title:
            Task.objects.create(title=title)
        return redirect("task_list")

    context = {"tasks": tasks}
    return render(request, "taskapp/task_list.html", context)


#view for updating an existing task's details
def task_update(request, pk):
    # Retrieve the specific task or return a 404 error if it doesn't exist
    task = get_object_or_404(Task, pk=pk)

    if request.method == "POST":
        task.title = request.POST.get("title", task.title)
        task.description = request.POST.get("description", task.description)
        task.completed = "completed" in request.POST
        task.save()
        return redirect("task_list")

    context = {"task": task}
    return render(request, "taskapp/task_update.html", context)


#handling the deletion of a task
def task_delete(request, pk):
    task = get_object_or_404(Task, pk=pk)

    if request.method == "POST":
        task.delete()
        return redirect("task_list")

    context = {"task": task}
    return render(request, "taskapp/task_delete.html", context)
