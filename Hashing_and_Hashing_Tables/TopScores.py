import unittest


def sort_scores(unsorted_scores, highest_possible_score):

    # Create a list of 0s from the lowest score to the high score possible
    score_counts = [0] * (highest_possible_score + 1)
    
    # Fill in score_counts
    for score in unsorted_scores:
        score_counts[score] += 1
    
    #Final sorted list
    sorted_scores = []
    
    for score in range(len(score_counts) - 1, -1, -1):
        # Assign value to count to tell us the number of times the number occurs 
        count = score_counts[score]
    
        
        #for the number of times the item occurs
        for occurences in range(count):
            
            sorted_scores.append(score)


    return sorted_scores

# Tests

class Test(unittest.TestCase):

    def test_no_scores(self):
        actual = sort_scores([], 100)
        expected = []
        self.assertEqual(actual, expected)

    def test_one_score(self):
        actual = sort_scores([55], 100)
        expected = [55]
        self.assertEqual(actual, expected)

    def test_two_scores(self):
        actual = sort_scores([30, 60], 100)
        expected = [60, 30]
        self.assertEqual(actual, expected)

    def test_many_scores(self):
        actual = sort_scores([37, 89, 41, 65, 91, 53], 100)
        expected = [91, 89, 65, 53, 41, 37]
        self.assertEqual(actual, expected)

    def test_repeated_scores(self):
        actual = sort_scores([20, 10, 30, 30, 10, 20], 100)
        expected = [30, 30, 20, 20, 10, 10]
        self.assertEqual(actual, expected)


unittest.main(verbosity=2)