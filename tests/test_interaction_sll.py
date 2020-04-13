import unittest

from core.basic_sll_classes import SingleLinkedList, SingleLinkedListNode
from core.interaction_sll_classes import InteractSingleLinkedLists


class TestIntersectionSSL(unittest.TestCase):

    def setUp(self):
        first_sll_head_node = SingleLinkedListNode(value=1)
        first_sll = SingleLinkedList(head=first_sll_head_node)
        first_sll.append_new_node(value=3)
        first_sll.append_new_node(value=4)
        first_sll.append_new_node(value=5)

        second_sll_head_node = SingleLinkedListNode(value=2)
        second_sll = SingleLinkedList(head=second_sll_head_node)
        second_sll.append_new_node(value=4)
        second_sll.append_new_node(value=5)

        third_sll_head_node = SingleLinkedListNode(value=1)
        third_sll = SingleLinkedList(head=third_sll_head_node)
        third_sll.append_new_node(value=3)
        third_sll.append_new_node(value=5)

        fourth_sll_head_node = SingleLinkedListNode(value=1)
        fourth_sll = SingleLinkedList(head=fourth_sll_head_node)
        fourth_sll.append_new_node(value=3)
        fourth_sll.append_new_node(value=5)

        fifth_sll_head_node = SingleLinkedListNode(value=11)
        fifth_sll = SingleLinkedList(head=fifth_sll_head_node)
        fifth_sll.append_new_node(value=12)
        fifth_sll.append_new_node(value=13)

        empty_sll = SingleLinkedList()

        self.payload = {
            'first_sll': first_sll,
            'second_sll': second_sll,
            'third_sll': third_sll,
            'fourth_sll': fourth_sll,
            'fifth_sll': fifth_sll,
            'empty_sll': empty_sll,
        }

    def test_get_intersection__when_first_sll_is_bigger_than_second_sll(self):
        first_sll = self.payload.get('first_sll')
        second_sll = self.payload.get('second_sll')
        self.assertTrue(first_sll.get_length() > second_sll.get_length())
        compare_classes_instance = InteractSingleLinkedLists(first_single_linked_list=first_sll, second_single_linked_list=second_sll)
        intersection_node = compare_classes_instance.get_intersection()
        self.assertEqual(intersection_node.value, 4)

    def test_get_intersection__when_first_sll_is_less_than_second_sll(self):
        first_sll = self.payload.get('first_sll')
        second_sll = self.payload.get('second_sll')
        self.assertTrue(first_sll.get_length() > second_sll.get_length())
        compare_classes_instance = InteractSingleLinkedLists(first_single_linked_list=second_sll, second_single_linked_list=first_sll)
        intersection_node = compare_classes_instance.get_intersection()
        self.assertEqual(intersection_node.value, 4)

    def test_get_intersection__when_first_sll_and_second_sll_have_equal_length(self):
        second_sll = self.payload.get('second_sll')
        third_sll = self.payload.get('third_sll')
        self.assertTrue(second_sll.get_length() == third_sll.get_length())
        compare_classes_instance = InteractSingleLinkedLists(first_single_linked_list=second_sll, second_single_linked_list=third_sll)
        intersection_node = compare_classes_instance.get_intersection()
        self.assertEqual(intersection_node.value, 5)

    def test_get_intersection__when_there_is_no_intersection(self):
        first_sll = self.payload.get('first_sll')
        fifth_sll = self.payload.get('fifth_sll')
        compare_classes_instance = InteractSingleLinkedLists(first_single_linked_list=first_sll, second_single_linked_list=fifth_sll)
        intersection_node = compare_classes_instance.get_intersection()
        self.assertIsNone(intersection_node)

    def test_get_intersection__when_first_node_is_intersection(self):
        third_sll = self.payload.get('third_sll')
        fourth_sll = self.payload.get('fourth_sll')
        compare_classes_instance = InteractSingleLinkedLists(first_single_linked_list=third_sll, second_single_linked_list=fourth_sll)
        intersection_node = compare_classes_instance.get_intersection()
        self.assertEqual(intersection_node.value, 1)

    def test_get_intersection__when_one_of_ssl_is_empty(self):
        first_sll = self.payload.get('first_sll')
        empty_sll = self.payload.get('empty_sll')
        compare_classes_instance = InteractSingleLinkedLists(first_single_linked_list=first_sll, second_single_linked_list=empty_sll)
        intersection_node = compare_classes_instance.get_intersection()
        self.assertIsNone(intersection_node)


class TestMergeSSL(unittest.TestCase):

    def setUp(self):
        first_sll_head_node = SingleLinkedListNode(value=1)
        first_sll = SingleLinkedList(head=first_sll_head_node)
        first_sll.append_new_node(value=3)
        first_sll.append_new_node(value=3)
        first_sll.append_new_node(value=4)
        first_sll.append_new_node(value=5)
        first_sll.append_new_node(value=5)
        first_sll.append_new_node(value=5)

        second_sll_head_node = SingleLinkedListNode(value=1)
        second_sll = SingleLinkedList(head=second_sll_head_node)
        second_sll.append_new_node(value=2)
        second_sll.append_new_node(value=2)
        second_sll.append_new_node(value=4)
        second_sll.append_new_node(value=5)
        second_sll.append_new_node(value=6)
        second_sll.append_new_node(value=7)

        empty_sll = SingleLinkedList()

        resulted_sll_string = '1->1->2->2->3->3->4->4->5->5->5->5->6->7'

        self.payload = {
            'first_sll': first_sll,
            'second_sll': second_sll,
            'empty_sll': empty_sll,
            'resulted_sll_string': resulted_sll_string
        }

    def test_merge_sll(self):
        first_sll = self.payload.get('first_sll')
        second_sll = self.payload.get('second_sll')
        compare_classes_instance = InteractSingleLinkedLists(first_single_linked_list=first_sll, second_single_linked_list=second_sll)
        resulted_sll = compare_classes_instance.merge()
        self.assertEqual(resulted_sll.get_length(), 14)
        self.assertEqual(resulted_sll.get_string_of_values(), self.payload.get('resulted_sll_string'))

    def test_merge_sll__when_one_of_lists_is_empty(self):
        first_sll = self.payload.get('first_sll')
        empty_sll = self.payload.get('empty_sll')
        compare_classes_instance = InteractSingleLinkedLists(first_single_linked_list=first_sll, second_single_linked_list=empty_sll)
        resulted_sll = compare_classes_instance.merge()
        self.assertEqual(resulted_sll.get_length(), first_sll.get_length())
        self.assertEqual(resulted_sll.get_string_of_values(), first_sll.get_string_of_values())
