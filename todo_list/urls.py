from django.urls import path

from todo_list.views import (
    TaskListView,
    TagListView,
    TagCreateView, TagUpdateView, TagDeleteView
)

urlpatterns = [
    path("", TaskListView.as_view(), name="task_list"),
    path("tags/", TagListView.as_view(), name="tag_list"),
    path("create-tag/", TagCreateView.as_view(), name="create_tag"),
    path("tags/update/<int:pk>/", TagUpdateView.as_view(), name="update_tag"),
    path("tags/delete/<int:pk>/", TagDeleteView.as_view(), name="delete_tag"),
]

app_name = "todo_list"
