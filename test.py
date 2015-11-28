import unittest

def HelloWorld():
  return "Hello World"

class TestStringMethods(unittest.TestCase):

  def test_helloworld(self):
      self.assertEqual('Hello World', HelloWorld())

if __name__ == '__main__':
    unittest.main()