"""
A text script for cap.py
"""

import unittest
import cap

class TestCap(unittest.TestCase):
    
    def test_one_word(self):
        text = 'hello'
        result = cap.cap_text(text)
        self.assertEqual(result, 'Hello')


    def test_two_words(self):
        text = 'hello world'
        result = cap.cap_text(text)
        self.assertEqual(result, 'Hello World')

if __name__ == '__main__':
    unittest.main()