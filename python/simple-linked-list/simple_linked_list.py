class Node(object):
    def __init__(self, value):
        self._value = value
        self._next = None

    def value(self):
        return self._value

    def next(self):
        return self._next


class LinkedList(object):
    def __init__(self, values=[]):
        self._head = None
        for value in values:
            self.push(value)

    def __len__(self):
        length = 0
        node = self._head
        while node:
            length += 1
            node = node._next
        return length

    def head(self):
        if self._head:
            return self._head
        else:
            raise EmptyListException

    def push(self, value):
        new_head = Node(value)
        if self._head:
            new_head._next = self._head
        self._head = new_head

    def pop(self):
        if self._head:
            value = self._head.value()
            self._head = self._head._next
            return value
        else:
            raise EmptyListException

    def __iter__(self):
        self.iter_next = self._head
        return self

    def __next__(self):
        if self.iter_next:
            value = self.iter_next.value()
            self.iter_next = self.iter_next._next
            return value
        else:
            raise StopIteration

    def reversed(self):
        values = list(self)
        return LinkedList(values)


class EmptyListException(Exception):
    pass

