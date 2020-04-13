import unittest
from core.basic_sll_classes import SingleLinkedListNode, SingleLinkedList


class TestBasicFuncionality(unittest.TestCase):
    def setUp(self):
        head_node = SingleLinkedListNode(value=1)
        single_linked_list = SingleLinkedList(head=head_node)
        single_linked_list.append_new_node(2)
        single_linked_list.append_new_node(3)
        self.payload = {
            'head_node': head_node,
            'single_linked_list': single_linked_list,
        }

    def test_adding_new_node(self):
        test_sll = self.payload.get('single_linked_list')
        self.assertEqual(test_sll.get_length(), 3)
        test_sll.append_new_node(4)
        self.assertEqual(test_sll.get_length(), 4)
