import unittest
from password_manager import logic

class TestPasswordManager(unittest.TestCase):
    def test_add_password(self):
        logic.add_password('example.com', 'user', 'password123', 'description')
        password = logic.view_password('example.com')
        self.assertEqual(password, 'password123')

if __name__ == '__main__':
    unittest.main()
