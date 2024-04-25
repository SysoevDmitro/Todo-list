from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import TaskForm, TagForm
from .models import Task, Tag


def index(request):
    num_tasks = Task.objects.count()
    num_tags = Tag.objects.count()

    content = {"num_tasks": num_tasks, "num_tags": num_tags}

    return render(request, "task_manager/index.html", context=content)


class TaskListView(generic.ListView):
    model = Task

    def get_queryset(self):
        return Task.objects.order_by("is_done", "-created")


class TaskCreateView(generic.CreateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy("task_manager:task-list")


class TaskUpdateView(generic.UpdateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy("task_manager:task-list")


class TaskDeleteView(generic.DeleteView):
    model = Task
    success_url = reverse_lazy("task_manager:task-list")


class TagListView(generic.ListView):
    model = Tag


class TagCreateView(generic.CreateView):
    model = Tag
    form_class = TagForm
    success_url = reverse_lazy("task_manager:tag-list")


class TagUpdateView(generic.UpdateView):
    model = Tag
    form_class = TagForm
    success_url = reverse_lazy("task_manager:tag-list")


class TagDeleteView(generic.DeleteView):
    model = Tag
    success_url = reverse_lazy("task_manager:tag-list")


def toggle_task(request, pk):
    task = get_object_or_404(Task, pk=pk)

    # Toggle the is_done status
    task.is_done = not task.is_done
    task.save()

    return HttpResponseRedirect(reverse_lazy("task_manager:task-list"))
