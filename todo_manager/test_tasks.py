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
        
    def test_title_upper(self): # TDD test 1
        task = Task("Supermarket Shopping")
        self.assertEqual(task.title_upper(), "SUPERMARKET SHOPPING") # verify task title is correctly set and produces expected result

if __name__ == '__main__':
    unittest.main()