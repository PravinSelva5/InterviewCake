---------------------------
          ARRAY 
---------------------------

The pros of arrays include: fast lookups (O(1)) and fast appends O(1)
The cons of arrays include: fixed size and costly inserts & deletes because you need to scoot the other elements to fill in or close gaps, which takes worst case O(N)

---------------------------
        ARRAY SLICING
---------------------------

Remember when you are slicing:
    - You are allocating a new make_list
    - copying the elements from the original list to the new list

Slicing worst case takes O(n) time and O(n) space.


---------------------------
    IN-PLACE ALGORITHMS
---------------------------

In-place functions modifies data structures or objects outside of its own stack frame. Because of this, the changes made by the function remain after the call completes.
They're considered destructive because the original input is "destroyed", during the function call.

In-place function will ONLY create additional variables that are O(1) space.

Out-place function copy any data structures or objects before manipulating and changing them

In many languages, primitive values such as ints, floats and characters are COPIED when passed as arguments, and more COMPLEX STRUCTS such as lists, heaps, or hash tables are PASSED BY REFERENCE.

Working in-place saves time and space but YOU NEED TO BE CAREFUL because your input is destroyed or altered, which can affect the CODE outisde of your function.


--------------------------------

In general, only use in-place when you're space constrained or you're positive you don't need the original input anymore, even for debugging.