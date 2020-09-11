'''
My cake shop is so popular, I'm adding some tables and hiring wait staff so folks can have a cute sit-down cake-eating experience.

I have two registers: one for take-out orders, and the other for the other folks eating inside the cafe. All the customer orders get combined into one list for the kitchen, where they should be handled first-come, first-served.

Recently, some customers have been complaining that people who placed orders after them are getting their food first. Yikes—that's not good for business!

To investigate their claims, one afternoon I sat behind the registers with my laptop and recorded:

The take-out orders as they were entered into the system and given to the kitchen. (take_out_orders)
The dine-in orders as they were entered into the system and given to the kitchen. (dine_in_orders)
Each customer order (from either register) as it was finished by the kitchen. (served_orders)
Given all three lists, write a function to check that my service is first-come, first-served. All food should come out in the same order customers requested it.

We'll represent each customer order as a unique integer.

RECURSIVE SOLUTION FROM WEBSITE
'''

import unittest

def is_first_come_first_served(take_out_orders, dine_in_orders, served_orders, take_out_orders_index=0, dine_in_orders_index=0,
                               served_orders_index=0):
    # Base case we've hit the end of served_orders
    if served_orders_index == len(served_orders):
        return True

    # If we still have orders in take_out_orders
    # and the current order in take_out_orders is the same
    # as the current order in served_orders
    if ((take_out_orders_index < len(take_out_orders)) and
            take_out_orders[take_out_orders_index] == served_orders[served_orders_index]):
        take_out_orders_index += 1

    # If we still have orders in dine_in_orders
    # and the current order in dine_in_orders is the same
    # as the current order in served_orders
    elif ((dine_in_orders_index < len(dine_in_orders)) and
            dine_in_orders[dine_in_orders_index] == served_orders[served_orders_index]):
        dine_in_orders_index += 1

    # If the current order in served_orders doesn't match
    # the current order in take_out_orders or dine_in_orders, then we're not
    # serving in first-come, first-served order.
    else:
        return False

    # The current order in served_orders has now been "accounted for"
    # so move on to the next one
    served_orders_index += 1
    return is_first_come_first_served(
        take_out_orders, dine_in_orders, served_orders,
        take_out_orders_index, dine_in_orders_index, served_orders_index)

'''
An iterative solutiion that takes the above space complexity from O(n) to O(1)
'''

def is_first_come_first_served(take_out_orders, dine_in_orders, served_orders):
    take_out_orders_index = 0
    dine_in_orders_index = 0
    take_out_orders_max_index = len(take_out_orders) - 1
    dine_in_orders_max_index = len(dine_in_orders) - 1
    
    for order in served_orders:
        # If we still have orders in take_out_orders
        # and the current order in take_out_orders is the same
        # as the current order in served_orders
        if take_out_orders_index <= take_out_orders_max_index and order == take_out_orders[take_out_orders_index]:
            take_out_orders_index += 1
        
        # If we still have orders in dine_in_orders
        # and the current order in dine_in_orders is the same
        # as the current order in served_orders
        
        elif dine_in_orders_index <= dine_in_orders_max_index and order == dine_in_orders[dine_in_orders_index]:
            dine_in_orders_index += 1
            
        else:
            return False
    
    # Check for extra orders at the end of take_out_orders or dine_in_orders
    
    if dine_in_orders_index != len(dine_in_orders) or take_out_orders_index != len(take_out_orders):
        return False
    
    return True

# Tests
class Test(unittest.TestCase):

    def test_both_registers_have_same_number_of_orders(self):
        result = is_first_come_first_served([1, 4, 5], [2, 3, 6], [1, 2, 3, 4, 5, 6])
        self.assertTrue(result)

    def test_registers_have_different_lengths(self):
        result = is_first_come_first_served([1, 5], [2, 3, 6], [1, 2, 6, 3, 5])
        self.assertFalse(result)

    def test_one_register_is_empty(self):
        result = is_first_come_first_served([], [2, 3, 6], [2, 3, 6])
        self.assertTrue(result)

    def test_served_orders_is_missing_orders(self):
        result = is_first_come_first_served([1, 5], [2, 3, 6], [1, 6, 3, 5])
        self.assertFalse(result)

    def test_served_orders_has_extra_orders(self):
        result = is_first_come_first_served([1, 5], [2, 3, 6], [1, 2, 3, 5, 6, 8])
        self.assertFalse(result)

    def test_one_register_has_extra_orders(self):
        result = is_first_come_first_served([1, 9], [7, 8], [1, 7, 8])
        self.assertFalse(result)

    def test_one_register_has_unserved_orders(self):
        result = is_first_come_first_served([55, 9], [7, 8], [1, 7, 8, 9])
        self.assertFalse(result)

    def test_order_numbers_are_not_sequential(self):
        result = is_first_come_first_served([27, 12, 18], [55, 31, 8], [55, 31, 8, 27, 12, 18])
        self.assertTrue(result)

unittest.main(verbosity=2)

