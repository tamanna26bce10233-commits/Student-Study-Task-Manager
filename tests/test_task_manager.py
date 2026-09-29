import unittest

from modules.task import Task
from modules.validation import validate_task_title


class TestTaskManager(unittest.TestCase):

    def test_task_starts_as_pending(self):
        task = Task("Study Python")
        self.assertFalse(task.completed)

    def test_valid_task_title(self):
        valid, result = validate_task_title("Study Python")
        self.assertTrue(valid)
        self.assertEqual(result, "Study Python")

    def test_empty_task_title(self):
        valid, result = validate_task_title("   ")
        self.assertFalse(valid)


if __name__ == "__main__":
    unittest.main()
    