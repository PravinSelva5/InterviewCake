'''
Greedy Algorithm builds up a solution by choosing the best option that looks best AT EVERY STEP
'''

def get_max_profit(stock_prices):
    
    # Calculate the max profit
    
    anchor = 0
    max_profit = -1000
    counter = 0
    
    if len(stock_prices) <= 1:
        raise Exception("Not a valid input")
    
    for stock in stock_prices:
        
        anchor = stock
        counter += 1
        
        if counter > len(stock_prices):
            break
        
        for price in range(counter, len(stock_prices)):
            
            if (stock_prices[price] - anchor) >= max_profit:
                
                max_profit = stock_prices[price] - anchor
            
            elif (stock_prices[price] - anchor) < 0:
                max_profit = max(max_profit, stock_prices[price] - anchor)
            else:
                continue
        
    return max_profit


# Tests

import unittest

class Test(unittest.TestCase):

    def test_price_goes_up_then_down(self):
        actual = get_max_profit([1, 5, 3, 2])
        expected = 4
        self.assertEqual(actual, expected)

    def test_price_goes_down_then_up(self):
        actual = get_max_profit([7, 2, 8, 9])
        expected = 7
        self.assertEqual(actual, expected)

    def test_price_goes_up_all_day(self):
        actual = get_max_profit([1, 6, 7, 9])
        expected = 8
        self.assertEqual(actual, expected)

    def test_price_goes_down_all_day(self):
        actual = get_max_profit([9, 7, 4, 1])
        expected = -2
        self.assertEqual(actual, expected)

    def test_price_stays_the_same_all_day(self):
        actual = get_max_profit([1, 1, 1, 1])
        expected = 0
        self.assertEqual(actual, expected)

    def test_error_with_empty_prices(self):
        with self.assertRaises(Exception):
            get_max_profit([])

    def test_error_with_one_price(self):
        with self.assertRaises(Exception):
            get_max_profit([1])


unittest.main(verbosity=2)