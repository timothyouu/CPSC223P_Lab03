# Name: Timothy Ou
# Date: 02/10/2026
# Purpose: Created main file that prints the menu and 
# takes user input to interact with the functions in 
# the data structures file

from data_structure import *

# menu driven interface with list, stack, and queue operations
def show_menu():
    my_list = []
    stack = []
    queue = []

    while True:
        print("\n*** MAIN MENU ***")
        print("1. List Operations")
        print("2. Stack Operations")
        print("3. Queue Operations")
        print("4. Exit")

        choice1 = input("Enter your choice: ")

        if choice1 == '1':
            while True:
                print("\n*** LIST OPERATIONS ***")
                print("1. Append item")
                print("2. Insert item")
                print("3. Remove item")
                print("4. Pop item")
                print("5. Clear list")
                print("6. Sort list")
                print("7. Reverse list")
                print("8. Index of item")
                print("9. Count of item")
                print("10. Slice list")
                print("11. Delete item (using del)")
                print("12. Return to Main Menu")

                choice2 = input("Enter your choice: ")

                if choice2 == '1':
                    item = input("Enter item to append: ")
                    my_list = append_item(my_list, item)
                    print("***Item '" + str(item) + "' appended successfully! ***")
                elif choice2 == '2':
                    item = input("Enter item to insert: ")
                    idx = int(input("Enter index: "))
                    my_list = insert_item(my_list, idx, item)
                    print("***Item '" + str(item) + "' inserted at index " + str(idx) + " successfully! ***")
                elif choice2 == '3':
                    item = input("Enter item to remove: ")
                    my_list = remove_item(my_list, item)
                    print("***First occurrence of '" + str(item) + "' removed successfully! ***")
                elif choice2 == '4':
                    idx_input = input("Enter index to pop: ")
                    if idx_input:
                        idx = int(idx_input)
                    else:
                        idx = -1
                    my_list = pop_item(my_list, idx)
                    print("***Item at index " + str(idx) + " popped successfully! ***")
                elif choice2 == '5':
                    my_list = clear_list(my_list)
                    print("***List cleared successfully! ***")
                elif choice2 == '6':
                    my_list = sort_list(my_list)
                    print("***List sorted successfully! ***")
                elif choice2 == '7':
                    my_list = reverse_list(my_list)
                    print("***List reversed successfully! ***")
                elif choice2 == '8':
                    item = input("Enter item to find: ")
                    result = index_of_item(my_list, item)
                    print("***Index of '" + str(item) + "' found successfully: " + str(result[0]) + " ***")
                elif choice2 == '9':
                    item = input("Enter item to count: ")
                    result = count_item(my_list, item)
                    print("***Count for '" + str(item) + "' calculated successfully: " + str(result[0]) + " ***")
                elif choice2 == '10':
                    start = int(input("Enter start index: "))
                    end = int(input("Enter end index: "))
                    sliced = slice_list(my_list, start, end)
                    print("***Portion sliced successfully: " + str(sliced) + " ***")
                elif choice2 == '11':
                    break
                
                print("***CURRENT LIST: " + str(my_list) + " ***")

        elif choice1 == '2':
            while True:
                print("\n*** STACK OPERATIONS ***")
                print("1. Push item")
                print("2. Pop item")
                print("3. Return to Main Menu")

                choice3 = input("Enter your choice: ")

                if choice3 == '1':
                    item = input("Enter item to push: ")
                    stack = push_stack(stack, item)
                    print("***Item '" + str(item) + "' pushed successfully!***")
                elif choice3 == '2':
                    stack = pop_stack(stack)
                    print("***Item popped successfully!***")
                elif choice3 == '3':
                    break
                
                print("***CURRENT STACK: " + str(stack) + " ***")

        elif choice1 == '3':
            while True:
                print("\n*** QUEUE OPERATIONS ***")
                print("1. Enqueue item")
                print("2. Dequeue item")
                print("3. Return to Main Menu")

                choice4 = input("Enter your choice: ")

                if choice4 == '1':
                    item = input("Enter item to enqueue: ")
                    queue = enqueue(queue, item)
                    print("***Item '" + str(item) + "' enqueued successfully!***")
                elif choice4 == '2':
                    queue = dequeue(queue)
                    print("***Item dequeued successfully!***")
                elif choice4 == '3':
                    break
                
                print("***CURRENT QUEUE: " + str(queue) + " ***")
        elif choice1 == '4':
            print("***Exiting program...***")
            break