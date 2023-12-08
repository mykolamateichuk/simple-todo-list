from django.test import TestCase
from django.urls import reverse_lazy

from todo_list.models import Task, Tag


class ChangeStatusViewTest(TestCase):
    def setUp(self) -> None:
        tag = Tag.objects.create(
            name="tag"
        )

        for i in range(2):
            Task.objects.create(
                content=f"Task {i}",
                is_done=True if i % 2 == 0 else False
            ).tags.set((tag, ))

    def test_changes_status(self) -> None:
        response1 = self.client.get(reverse_lazy("todo_list:change_status",
                                                 kwargs={"pk": 1}))
        task1 = Task.objects.first()
        self.assertEqual(task1.is_done, False)

        response2 = self.client.get(reverse_lazy("todo_list:change_status",
                                                 kwargs={"pk": 1}))
        task2 = Task.objects.last()
        self.assertEqual(task2.is_done, True)
