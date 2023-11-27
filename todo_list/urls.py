from django.urls import path

from todo_list.views import TaskListView, TagListView

urlpatterns = [
    path("", TaskListView.as_view(), name="task_list"),
]

app_name = "todo_list"
