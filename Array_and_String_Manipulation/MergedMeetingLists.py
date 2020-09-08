import unittest

'''
------------
COMPLEXITY
------------
O(nlgn) time and O(n)O(n) space.

'''

def merge_ranges(meetings):

    # sort meeting times
    sorted_meeting_times = sorted(meetings)
    
    #List that will contain output 
    merged_lists = [sorted_meeting_times[0]]
    
    for current_meeting_start, current_meeting_end in sorted_meeting_times[1:]:
        last_merged_meeting_start, last_merged_meeting_end = merged_lists[-1]
        
        # If the last merged meeting time overlaps with the current meeting time,
        # Us the later end time of both
        
        if (current_meeting_start <= last_merged_meeting_end):
            merged_lists[-1] = (last_merged_meeting_start, max(last_merged_meeting_end, current_meeting_end))
        
        else:
            # Add the current meeting because it doesn't overlap
            merged_lists.append((current_meeting_start,current_meeting_end))
    

    return merged_lists



# Tests

class Test(unittest.TestCase):

    def test_meetings_overlap(self):
        actual = merge_ranges([(1, 3), (2, 4)])
        expected = [(1, 4)]
        self.assertEqual(actual, expected)

    def test_meetings_touch(self):
        actual = merge_ranges([(5, 6), (6, 8)])
        expected = [(5, 8)]
        self.assertEqual(actual, expected)

    def test_meeting_contains_other_meeting(self):
        actual = merge_ranges([(1, 8), (2, 5)])
        expected = [(1, 8)]
        self.assertEqual(actual, expected)

    def test_meetings_stay_separate(self):
        actual = merge_ranges([(1, 3), (4, 8)])
        expected = [(1, 3), (4, 8)]
        self.assertEqual(actual, expected)

    def test_multiple_merged_meetings(self):
        actual = merge_ranges([(1, 4), (2, 5), (5, 8)])
        expected = [(1, 8)]
        self.assertEqual(actual, expected)

    def test_meetings_not_sorted(self):
        actual = merge_ranges([(5, 8), (1, 4), (6, 8)])
        expected = [(1, 4), (5, 8)]
        self.assertEqual(actual, expected)

    def test_one_long_meeting_contains_smaller_meetings(self):
        actual = merge_ranges([(1, 10), (2, 5), (6, 8), (9, 10), (10, 12)])
        expected = [(1, 12)]
        self.assertEqual(actual, expected)

    def test_sample_input(self):
        actual = merge_ranges([(0, 1), (3, 5), (4, 8), (10, 12), (9, 10)])
        expected = [(0, 1), (3, 8), (9, 12)]
        self.assertEqual(actual, expected)


unittest.main(verbosity=2)