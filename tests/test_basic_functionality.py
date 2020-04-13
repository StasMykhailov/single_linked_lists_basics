import unittest
from core.basic_sll_classes import SingleLinkedListNode, SingleLinkedList


class TestBasicFuncionality(unittest.TestCase):
    def setUp(self):
        head_node = SingleLinkedListNode(value=1)
        single_linked_list = SingleLinkedList(head=head_node)
        single_linked_list.append_new_node(2)
        single_linked_list.append_new_node(3)
        single_linked_list_string = '1->2->3'
        reversed_single_linked_list_string = '3->2->1'
        self.payload = {
            'head_node': head_node,
            'single_linked_list': single_linked_list,
            'single_linked_list_string': single_linked_list_string,
            'reversed_single_linked_list_string': reversed_single_linked_list_string,
        }

    def test_get_length_method(self):
        test_sll = self.payload.get('single_linked_list')
        self.assertEqual(test_sll.get_length(), 3)

    def test_get_strings_of_values_method(self):
        test_sll = self.payload.get('single_linked_list')
        self.assertEqual(test_sll.get_string_of_values(), self.payload.get('single_linked_list_string'))

    def test_adding_new_node(self):
        test_sll = self.payload.get('single_linked_list')
        self.assertEqual(test_sll.get_length(), 3)
        test_sll.append_new_node(4)
        self.assertEqual(test_sll.get_length(), 4)

    def test_reverse(self):
        head_node = self.payload.get('head_node')
        test_sll = self.payload.get('single_linked_list')
        self.assertEqual(test_sll.head, head_node)
        self.assertEqual(test_sll.get_string_of_values(), self.payload.get('single_linked_list_string'))
        test_sll.reverse_list()
        self.assertEqual(test_sll.head.value, 3)
        self.assertEqual(test_sll.get_string_of_values(), self.payload.get('reversed_single_linked_list_string'))
