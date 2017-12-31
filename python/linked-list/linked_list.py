class Node(object):
    def __init__(self, value, next_=None, previous=None):
        self.value = value
        self.next_ = next_
        self.previous = previous


class LinkedList(object):
    def __init__(self):
        self.head = None
        self.tail = None

    def push(self, value):
        new_head = Node(value)
        if self.head:
            new_head.next_ = self.head
            self.head.previous = new_head
        self.head = new_head
        if not self.tail:
            self.tail = self.head

    def unshift(self, value):
        new_tail = Node(value)
        if self.tail:
            new_tail.previous = self.tail
            self.tail.next_ = new_tail
        self.tail = new_tail
        if not self.head:
            self.head = self.tail

    def pop(self):
        new_head = self.head.next_
        value = self.head.value
        self.head = new_head
        if self.head:
            self.head.previous = None
        return value

    def shift(self):
        new_tail = self.tail.previous
        value = self.tail.value
        self.tail = new_tail
        if new_tail:
            new_tail.next_ = None
        return value
