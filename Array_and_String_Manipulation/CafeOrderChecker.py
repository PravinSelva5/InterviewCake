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

'''

def is_first_come_first_served(take_out_orders, dine_in_orders, served_orders):
    
    
    # Initialize values
    total_orders = len(served_orders)
    #current_take_out_index = 0
    #current_dine_in_index = 0
    current_served_orders_index = 0
    
    while current_served_orders_index < total_orders:
      print(current_served_orders_index)
      if (served_orders[current_served_orders_index] == take_out_orders[0]) and (not take_out_orders):
        current_served_orders_index += 1
        del take_out_orders[0]
        print(take_out_orders)
        
      elif (served_orders[current_served_orders_index] == dine_in_orders[0]) and (not dine_in_orders):
        current_served_orders_index += 1
        del dine_in_orders[0]
        print(dine_in_orders)
      else:
        continue
    
    if current_served_orders_index == total_orders:
      return True
    else:
      return False

output1 = is_first_come_first_served([17, 8, 24],[12, 19, 2],[17, 8, 12, 19, 24, 2])
print(output1)

