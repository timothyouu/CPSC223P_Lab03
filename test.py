# test.py
import unittest
import data_structure
from collections import deque

class Testfunctions(unittest.TestCase):

    def setUp(self):
        """Initialize test cases."""
        self.lst = [1, 2, 3, 4, 5]
        self.stack = []
        self.queue = deque([20,30,40,50,60])

    # List operations tests
    def test_append_item(self):
        data_structure.append_item(self.lst, 6)
        self.assertIn(6, self.lst)

    def test_insert_item(self):
        data_structure.insert_item(self.lst, 2, 99)
        self.assertEqual(self.lst[2], 99)

    def test_remove_item(self):
        data_structure.remove_item(self.lst, 3)
        self.assertNotIn(3, self.lst)

    def test_pop_item(self):
        item = data_structure.pop_item(self.lst)
        self.assertEqual(item, 5)

    def test_clear_list(self):
        data_structure.clear_list(self.lst)
        self.assertEqual(self.lst, [])

    def test_sort_list(self):
        unsorted_list = [3, 1, 4, 2]
        data_structure.sort_list(unsorted_list)
        self.assertEqual(unsorted_list, [1, 2, 3, 4])

    def test_reverse_list(self):
        data_structure.reverse_list(self.lst)
        self.assertEqual(self.lst, [5, 4, 3, 2, 1])

    def test_index_of_item(self):
        index = data_structure.index_of_item(self.lst, 3)
        self.assertEqual(index, 2)

    def test_count_item(self):
        self.lst.append(2)
        count = data_structure.count_item(self.lst, 2)
        self.assertEqual(count, 2)

    def test_slice_list(self):
        sliced = data_structure.slice_list(self.lst, 1, 4)
        self.assertEqual(sliced, [2, 3, 4])

    # Stack operations tests
    def test_push_stack(self):
        data_structure.push_stack(self.stack, 10)
        self.assertEqual(self.stack[-1], 10)

    def test_pop_stack(self):
        data_structure.push_stack(self.stack, 20)
        item = data_structure.pop_stack(self.stack)
        self.assertEqual(item, 20)

    # Queue operations tests
    def test_enqueue(self):
        data_structure.enqueue(self.queue, 15)
        self.assertEqual(self.queue[0], 20)
        self.assertEqual(self.queue[5], 15)

    def test_dequeue(self):
        data_structure.enqueue(self.queue, 30)
        item = data_structure.dequeue(self.queue)
        self.assertEqual(item, 20)

if __name__ == '__main__':
    unittest.main()
