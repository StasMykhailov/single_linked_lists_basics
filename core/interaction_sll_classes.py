from core.basic_sll_classes import SingleLinkedList


class InteractSingleLinkedLists:

    def __init__(self, first_single_linked_list, second_single_linked_list):
        self.first_single_linked_list = first_single_linked_list
        self.second_single_linked_list = second_single_linked_list

    def get_intersection(self):
        first_ssl_length = self.first_single_linked_list.get_length()
        second_ssl_length = self.second_single_linked_list.get_length()

        if not first_ssl_length or not second_ssl_length:
            return None

        first_ssl_start_node = self.first_single_linked_list.head
        second_ssl_start_node = self.second_single_linked_list.head
        if first_ssl_length > second_ssl_length:
            for _ in range(first_ssl_length-second_ssl_length):
                first_ssl_start_node = first_ssl_start_node.next_node
        if second_ssl_length > first_ssl_length:
            for _ in range(second_ssl_length-first_ssl_length):
                second_ssl_start_node = second_ssl_start_node.next_node

        while first_ssl_start_node and second_ssl_start_node:
            if first_ssl_start_node.value == second_ssl_start_node.value:
                return first_ssl_start_node
            first_ssl_start_node = first_ssl_start_node.next_node
            second_ssl_start_node = second_ssl_start_node.next_node

        return None

    def merge(self):
        first_ssl_length = self.first_single_linked_list.get_length()
        second_ssl_length = self.second_single_linked_list.get_length()

        if not first_ssl_length and not second_ssl_length:
            return SingleLinkedList()
        if not first_ssl_length and second_ssl_length:
            return self.second_single_linked_list
        if first_ssl_length and not second_ssl_length:
            return self.first_single_linked_list

        new_sll = SingleLinkedList()

        first_ssl_start_node = self.first_single_linked_list.head
        second_ssl_start_node = self.second_single_linked_list.head

        while first_ssl_start_node and second_ssl_start_node:
            min_value = min(first_ssl_start_node.value, second_ssl_start_node.value)
            new_sll.append_new_node(value=min_value)
            if first_ssl_start_node.value == min_value:
                first_ssl_start_node = first_ssl_start_node.next_node
            else:
                second_ssl_start_node = second_ssl_start_node.next_node

        if first_ssl_start_node:
            while first_ssl_start_node:
                new_sll.append_new_node(value=first_ssl_start_node.value)
                first_ssl_start_node = first_ssl_start_node.next_node
        if second_ssl_start_node:
            while second_ssl_start_node:
                new_sll.append_new_node(value=second_ssl_start_node.value)
                second_ssl_start_node = second_ssl_start_node.next_node

        return new_sll
