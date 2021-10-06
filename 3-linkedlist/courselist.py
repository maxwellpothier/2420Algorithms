from course import Course


class CourseList:

    def __init__(self):
        self.head = None
        self.list_size = 0
        self.current_gpa = 0.0
        self.list_is_sorted = True

    def insert(self, c: Course):
        self.list_size = self.list_size + 1
        if self.head == None:
            self.head = c
            return
        for current_node in self:
            pass
        current_node.set_next(c)

    def remove(self, number):
        return

    def remove_all(number):
        return

    def find(number):
        return

    def size(self):
        return self.list_size

    def calculate_gpa(self):
        return self.current_gpa

    def is_sorted(self):
        return self.list_is_sorted

    def __str__():
        return

    def __iter__(self):
        node = self.head
        while node is not None:
            yield node
            node = node.next

    def __next__(self):
        return
