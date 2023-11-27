from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic

from todo_list.forms import TagCreateForm, TaskCreateForm
from todo_list.models import Task, Tag


class TaskListView(generic.ListView):
    model = Task
    queryset = Task.objects.prefetch_related("tags")
    context_object_name = "tasks"


class TagListView(generic.ListView):
    model = Tag
    queryset = Tag.objects.prefetch_related("tasks")
    context_object_name = "tags"


class TagCreateView(generic.CreateView):
    model = Tag
    form_class = TagCreateForm
    success_url = reverse_lazy("todo_list:tag_list")


class TagUpdateView(generic.UpdateView):
    model = Tag
    form_class = TagCreateForm
    success_url = reverse_lazy("todo_list:tag_list")


class TagDeleteView(generic.DeleteView):
    model = Tag
    success_url = reverse_lazy("todo_list:tag_list")


class TaskCreateView(generic.CreateView):
    model = Task
    form_class = TaskCreateForm
    success_url = reverse_lazy("todo_list:task_list")


class TaskUpdateView(generic.UpdateView):
    model = Task
    form_class = TaskCreateForm
    success_url = reverse_lazy("todo_list:task_list")


class TaskDeleteView(generic.DeleteView):
    model = Task
    success_url = reverse_lazy("todo_list:task_list")


def change_task_status_view(request: HttpRequest, pk: int) -> HttpResponse:
    task = Task.objects.get(pk=pk)

    if task.is_done:
        task.is_done = False
    else:
        task.is_done = True

    task.save()

    return redirect(reverse_lazy("todo_list:task_list"))
