class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

    def set_next(self, node):
        self.next = node

    def __repr__(self):
        return self.val


class LinkedList:
    def __init__(self):
        self.head = None

    def __iter__(self):
        node = self.head
        while node is not None:
            yield node
            node = node.next

    def add_to_tail(self, node):
        if self.head == None:
            self.head = node
            return
        for current_node in self:
            pass
        current_node.set_next(node)

    def remove_from_head(self):
        if self.head == None:
            return None
        temp = self.head
        self.head = self.head.next
        return temp

    def __repr__(self):
        nodes = []
        for node in self:
            nodes.append(node.val)
        return " -> ".join(nodes)


def main():
    linked_list = LinkedList()
    linked_list.add_to_tail(Node("John"))
    linked_list.add_to_tail(Node("Max"))
    linked_list.add_to_tail(Node("Abby"))
    linked_list.add_to_tail(Node("Susan"))
    print("List:", linked_list)
    first = linked_list.remove_from_head()
    print("Removed:", first)
    print("List:", linked_list)


if __name__ == "__main__":
    main()
