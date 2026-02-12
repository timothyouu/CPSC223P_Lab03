# Name: Timothy Ou
# Date: 02/10/2026
# Purpose: Created data structure file that contains 
# all the operations for list, queue, and stack

# 1. Advanced List Operations:

def append_item(my_list, item):
    """add the item to the back of the list"""
    my_list.append(item)
    return my_list

def insert_item(my_list, index, item):
    """inserts an item at a specified index"""
    my_list.insert(index, item)
    return my_list

def remove_item(my_list, item):
    """removes the first occurence of the specified item"""
    if item in my_list: #learned from previous experience
        my_list.remove(item)
    return my_list

def pop_item(my_list, index=-1):
    """pops an item from the list at the given index"""
    if my_list: #learned from previous experience
        return my_list.pop(index)
    return None

def clear_list(my_list):
    """clears all items from the list"""
    my_list.clear()
    return my_list

def sort_list(my_list):
    """sorts the list in ascending order"""
    my_list.sort()
    return my_list

def reverse_list(my_list):
    """reverses the order of items in the list"""
    my_list.reverse()
    return my_list

def index_of_item(my_list, item):
    """returns the index of the first occurence of the item"""
    try: #learned from researching how to check for error if item not found
        return my_list.index(item)
    except ValueError:
        return -1

def count_item(my_list, item):
    """counts how many times of the item appears in the list"""
    return my_list.count(item)

def slice_list(my_list, start, end):
    """returns a slice of the list from start to end index"""
    return my_list[start:end]

def delete_item(my_list, item):
    """returns a list with the item removed using the 'del' keyword"""
    index_result = index_of_item(my_list, item)
    idx = index_result[0]
    if idx != -1:
        del my_list[idx]
    return my_list

# 2. Stack and Queue Implementations:

def push_stack(stack, item):
    """add item to the stack"""
    stack.append(item)
    return stack

def pop_stack(stack):
    """remove item from the stack"""
    if stack:
        return stack.pop()
    return None

def enqueue(queue, item):
    """add item to the queue"""
    queue.append(item)
    return queue

def dequeue(queue):
    """remove an element of a queue"""
    if queue:
        return queue.popleft() #using collections deque which requires popleft, had to research that
    return None