from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.views import generic

from todo_list.models import Task, Tag


class TaskListView(generic.ListView):
    model = Task
    queryset = Task.objects.prefetch_related("tags")
    context_object_name = "tasks"
