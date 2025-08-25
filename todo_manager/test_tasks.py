import unittest
from todo_manager.tasks import Task

class TestTask(unittest.TestCase):
    def test_task_creation(self):
        task = Task("Supermarket Shopping")
        self.assertEqual(task.title, "Supermarket Shopping")
        self.assertFalse(task.completed)

    def test_mark_complete(self):
        task = Task("Supermarket Shopping")
        task.mark_complete()
        self.assertTrue(task.completed)

if __name__ == '__main__':
    unittest.main()