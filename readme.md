# Lab 3: Python List Operations and Data Structure

## Purpose:
- Write a Python program that utilizes Python list operations, including advanced 
manipulation
- Employ loops, conditional statements, input/output, and functions to demonstrate various
data structure manipulations including stack and queues

## Instruction:

**Create the following functions with exact names, input, and purpose**
***All functions should be implemented using the built-in Python data structure manipulation functions. All functions should return a list***

1. Advanced List Operations:
    **Create `data_structure.py` and implement the following operations**

    - append_item(my_list, item): add the item to the back of the list
    - insert_item (my_list,, index, item): Inserts an item at a specified index.
    - remove_item (my_list,, item): Removes the first occurrence of the specified item.
    - pop_item (my_list,, index=-1): Pops an item from the list at the given index.
    - clear_list (my_list,): Clears all items from the list.
    - sort_list (my_list,): Sorts the list in ascending order.
    - reverse_list (my_list,): Reverses the order of items in the list.
    - index_of_item (my_list,, item): Returns the index of the first occurrence of the item.
    - count_item (my_list,, item): Counts how many times the item appears in the list.
    - slice_list (my_list,, start, end): Returns a slice of the list from start to end index.
    - delete_item(my_list,, item): Return a list with the item removed using the ‘del’ keyword

2. Stack and Queue Implementations:
    - push_stack(stack, item): add item to the stack
    - pop_stack(stack): remove item from the stack

    - enqueue(queue, item): add item to the queue
    - dequeue(queue): remove an element of a queue

3. Create an Interactive Menu
    1. Create a module `main.py` and import all functions from data_structure.py using:
        `from data_structure import *`

    2. Implement a menu-driven interface:
        - Menu Options:
            ▪ List Operations (Add, Insert, Remove, Pop, Clear, Sort, Reverse, Index, Count, Slice)
            ▪ Stack Operations (Push, Pop)
            ▪ Queue Operations (Enqueue, Dequeue)
            ▪ Exit

    3. Example:

*** MAIN MENU ***

1. List Operations
2. Stack Operations
3. Queue Operations
4. Exit
Enter your choice: 1
*** LIST OPERATIONS ***
1. Append item
2. Insert item
3. Remove item
4. Pop item
5. Clear list
6. Sort list
7. Reverse list
8. Index of item
9. Count of item
10. Slice list
11. Return to Main Menu
Enter your choice: 1
Enter item to append: apple 
***Item 'apple' appended successfully! ***
***CURRENT LIST: ['apple'] ***
Enter your choice: 11

*** MAIN MENU ***
2. Stack Operations
Enter your choice: 2
*** STACK OPERATIONS ***
1. Push item
2. Pop item
3. Return to Main Menu
Enter your choice: 1
Enter item to push: cherry
***Item 'cherry' pushed to stack!***
***CURRENT STACK: ['cherry'] ***

Enter your choice: 3 
*** MAIN MENU ***
3. Queue Operations
Enter your choice: 3
*** QUEUE OPERATIONS
1. Enqueue item
2. Dequeue item
3. Return to Main Menu
Enter your choice: 1
Enter item to enqueue: pear
***Item 'pear' enqueued!***
***CURRENT QUEUE: ['pear'] ***

Enter your choice: 3
*** MAIN MENU ***
4. Exit
Enter your choice: 4
***Exiting program...***