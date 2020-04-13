class SingleLinkedListNode:

    def __init__(self, value, next_node=None):
        self.value = value
        self.next_node = next_node

    def __str__(self):
        return str(self.value)


class SingleLinkedList:

    def __init__(self, head=None):
        self.head = head

    def get_length(self):
        next_node = self.head
        list_length = 0
        while next_node:
            list_length += 1
            next_node = next_node.next_node
        return list_length

    def get_string_of_values(self):
        next_node = self.head
        list_of_values = []
        while next_node:
            list_of_values.append(str(next_node.value))
            next_node = next_node.next_node
        if not list_of_values:
            return ''
        if len(list_of_values) == 1:
            return list_of_values[0]
        return '->'.join(list_of_values)

    def append_new_node(self, value):
        if value is None:
            return None
        new_node = SingleLinkedListNode(value=value)
        if self.head is None:
            self.head = new_node
            return new_node
        current_node = self.head
        while current_node.next_node:
            current_node = current_node.next_node
        current_node.next_node = new_node
        return new_node

    def reverse_list(self):
        if not self.head or not self.head.next_node:
            return self
        previous_node = self.head
        current_node = previous_node.next_node
        self.head.next_node = None
        while previous_node and current_node:
            current_node_next_node = current_node.next_node
            current_node.next_node = previous_node
            previous_node = current_node
            current_node = current_node_next_node
        self.head = previous_node
