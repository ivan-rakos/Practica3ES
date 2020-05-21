import unittest


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, False)
    def test_prueba(self):
        a=1

if __name__ == '__main__':
    unittest.main()
