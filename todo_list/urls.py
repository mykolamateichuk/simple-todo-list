from django.urls import path

from todo_list.views import (
    TaskListView,
    TagListView,
    TagCreateView
)

urlpatterns = [
    path("", TaskListView.as_view(), name="task_list"),
    path("tags/", TagListView.as_view(), name="tag_list"),
    path("create-tag/", TagCreateView.as_view(), name="create_tag"),
]

app_name = "todo_list"
