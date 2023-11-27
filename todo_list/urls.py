from django.urls import path

from todo_list.views import (
    TaskListView,
    TagListView,
    TagCreateView, TagUpdateView, TagDeleteView, TaskCreateView, TaskUpdateView, TaskDeleteView, change_task_status_view
)

urlpatterns = [
    path("", TaskListView.as_view(), name="task_list"),
    path("tags/", TagListView.as_view(), name="tag_list"),
    path("create-tag/", TagCreateView.as_view(), name="create_tag"),
    path("tags/update/<int:pk>/", TagUpdateView.as_view(), name="update_tag"),
    path("tags/delete/<int:pk>/", TagDeleteView.as_view(), name="delete_tag"),
    path("create-task/", TaskCreateView.as_view(), name="create_task"),
    path("tasks/update/<int:pk>/", TaskUpdateView.as_view(), name="update_task"),
    path("tasks/delete/<int:pk>/", TaskDeleteView.as_view(), name="delete_task"),
    path("tasks/change-status/<int:pk>/", change_task_status_view, name="change_status")
]

app_name = "todo_list"
