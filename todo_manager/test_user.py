import unittest
from todo_manager.user import User

class TestUser(unittest.TestCase):
    def test_create_user(self):
        user = User()
        # Example: test that a new user has no current user
        self.assertIsNone(user.get_current_user())

    def test_signup_and_login(self):
        user = User()
        # Simulate signup and login logic here
        # Use self.assertEqual, self.assertTrue, etc. to check results

if __name__ == '__main__':
    unittest.main()