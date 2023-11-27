from django.test import TestCase

from todo_list.models import Tag, Task


class TagModelTest(TestCase):
    def test_str(self) -> None:
        name = "tag"

        tag = Tag.objects.create(
            name=name
        )

        self.assertEqual(str(tag), name)


class TaskModelTest(TestCase):
    def test_str(self) -> None:
        content = "content"
        tag = Tag.objects.create(name="tag")

        task = Task.objects.create(
            content=content,
        )
        task.tags.set((tag,))

        self.assertEqual(str(task), content)
