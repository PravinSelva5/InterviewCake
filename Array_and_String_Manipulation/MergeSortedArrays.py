'''
In order to win the prize for most cookies sold, my friend Alice and I are going to merge our Girl Scout Cookies orders and enter as one unit.

Each order is represented by an "order id" (an integer).

We have our lists of orders sorted numerically already, in lists. Write a function to merge our lists of orders into one sorted list.
'''
import unittest


def merge_lists(my_list, alices_list):

    # Combine the sorted lists into one large sorted list
    length1, length2 = len(my_list), len(alices_list)
    joined_list = []
    i,j = 0,0
    
    while i < length1 and j < length2:
        if my_list[i] < alices_list[j]:
            joined_list.append(my_list[i])
            i += 1
        else:
            joined_list.append(alices_list[j])
            j += 1

    if i == length1:
      for j in range(j,length2):
        joined_list.append(alices_list[j])
    
    else:
      for i in range(i,length1):
        joined_list.append(my_list[i])
    return joined_list

# Tests

class Test(unittest.TestCase):

    def test_both_lists_are_empty(self):
        actual = merge_lists([], [])
        expected = []
        self.assertEqual(actual, expected)

    def test_first_list_is_empty(self):
        actual = merge_lists([], [1, 2, 3])
        expected = [1, 2, 3]
        self.assertEqual(actual, expected)

    def test_second_list_is_empty(self):
        actual = merge_lists([5, 6, 7], [])
        expected = [5, 6, 7]
        self.assertEqual(actual, expected)

    def test_both_lists_have_some_numbers(self):
        actual = merge_lists([2, 4, 6], [1, 3, 7])
        expected = [1, 2, 3, 4, 6, 7]
        self.assertEqual(actual, expected)

    def test_lists_are_different_lengths(self):
        actual = merge_lists([2, 4, 6, 8], [1, 7])
        expected = [1, 2, 4, 6, 7, 8]
        self.assertEqual(actual, expected)


unittest.main(verbosity=2)