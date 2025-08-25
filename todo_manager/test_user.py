import unittest
from todo_manager.user import User

class TestUser(unittest.TestCase):
    def test_create_user(self):
        user = User()
        self.assertIsNone(user.get_current_user())

if __name__ == '__main__':
    unittest.main()