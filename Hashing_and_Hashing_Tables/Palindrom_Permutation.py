'''
Write an efficient function that checks whether any permutation ↴ of an input string is a palindrome. ↴

You can assume the input string only contains lowercase letters.

Examples:

"civic" should return True
"ivicc" should return True
"civil" should return False
"livci" should return False
'''

import unittest


def has_palindrome_permutation(the_string):
    '''
    A Palindrome will have an even set of characters unless there's a middle charcter(s) which is always odd
    1. Loop through given string and count how many times a character is found in the string
    2. Add char to dictionary, if char is already present increment its value by 1 every time its found
    3. Check if all chars in the dictionary have even values except for atleast 1
    '''
    
    chars_dict = {}
    the_string_length = len(the_string)
    counter = 0
    
    # if string is empty
    if not the_string:
        return True

    for i in range(the_string_length):
        # count the number of times a character is present in a string
        if the_string[i] not in chars_dict:
            chars_dict[the_string[i]] = chars_dict.get(the_string[i], 0) + 1
        
        else:
            chars_dict[the_string[i]] += 1

    for key in chars_dict.keys():
        
        if chars_dict[key] % 2 == 0:
            counter += 1
    
    # Checks if atleast all except one char have even values
    if counter >= len(chars_dict) - 1: 
        return True
    else:
        return False

# Tests

class Test(unittest.TestCase):

    def test_permutation_with_odd_number_of_chars(self):
        result = has_palindrome_permutation('aabcbcd')
        self.assertTrue(result)

    def test_permutation_with_even_number_of_chars(self):
        result = has_palindrome_permutation('aabccbdd')
        self.assertTrue(result)

    def test_no_permutation_with_odd_number_of_chars(self):
        result = has_palindrome_permutation('aabcd')
        self.assertFalse(result)

    def test_no_permutation_with_even_number_of_chars(self):
        result = has_palindrome_permutation('aabbcd')
        self.assertFalse(result)

    def test_empty_string(self):
        result = has_palindrome_permutation('')
        self.assertTrue(result)

    def test_one_character_string(self):
        result = has_palindrome_permutation('a')
        self.assertTrue(result)


unittest.main(verbosity=2)