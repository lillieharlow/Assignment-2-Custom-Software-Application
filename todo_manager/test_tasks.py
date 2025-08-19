import unittest
from todo_manager.tasks import Task

class TestTask(unittest.TestCase):
    def test_task_creation(self):
        task = Task("Buy milk")
        self.assertEqual(task.title, "Buy milk")
        self.assertFalse(task.completed)

    def test_mark_complete(self):
        task = Task("Buy milk")
        task.mark_complete()
        self.assertTrue(task.completed)

if __name__ == '__main__':
    unittest.main()