'''
unit test allows you to write your own test program. And the goal is to send a specific set of data to your program, analyze the returned results, and then see if it actually gives you the expected result.
'''

# this is where we actually use the unit test.

import unittest
import cap_39

class testCap(unittest.TestCase):

    def test_one_word(self):

        text = 'python'
        result = cap_39.turn_cap(text)
        self.assertEqual(result, 'Python')

    def test_multiple_words(self):

        text = 'monty python'
        result = cap_39.turn_cap(text)
        self.assertEqual(result, 'Monty Python')


if __name__ == '__main__':
    unittest.main()

'''
and a lot of times in large companies you'll have someone in the QA department quality assurance actually writing these tests to make sure that your scripts work as they expect them to.
'''