import unittest

def reverse(list_of_chars):

    # Reverse the input list of chars in place
    last_index = len(list_of_chars) - 1
    list_length = len(list_of_chars)
    for first_index in range(list_length):
        
        if first_index > last_index:
            return list_of_chars
        else:
            list_of_chars[first_index], list_of_chars[last_index] = list_of_chars[last_index], list_of_chars[first_index]
            first_index += 1
            last_index -= 1


# Tests

class Test(unittest.TestCase):

    def test_empty_string(self):
        list_of_chars = []
        reverse(list_of_chars)
        expected = []
        self.assertEqual(list_of_chars, expected)

    def test_single_character_string(self):
        list_of_chars = ['A']
        reverse(list_of_chars)
        expected = ['A']
        self.assertEqual(list_of_chars, expected)

    def test_longer_string(self):
        list_of_chars = ['A', 'B', 'C', 'D', 'E']
        reverse(list_of_chars)
        expected = ['E', 'D', 'C', 'B', 'A']
        self.assertEqual(list_of_chars, expected)


unittest.main(verbosity=2)