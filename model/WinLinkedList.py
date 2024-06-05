from Rectangle import *


class Node:
    def __init__(self, rect):
        self.prev: Node = None
        self.next: Node = None
        self.rect: Rectangle = rect


class WinLL:
    def __init__(self):
        self.head: Node = None

    def __iter__(self):
        current = self.head
        while current:
            yield current
            current = current.next

    def add(self, new: Node):
        if self.head is None:
            self.head = new
        else:
            new.next = self.head
            self.head.prev = new
            self.head = new

        return self.head

    def remove(self, n: Node):
        if n == self.head:
            self.head = n.next
            if self.head is not None:
                self.head.prev = None
            return

        if n.prev is not None:
            n.prev.next = n.next

        if n.next is not None:
            n.next.prev = n.prev

        n.next = None
        n.prev = None

    def move_to_top(self, n: Node):
        if n == self.head:
            return

        if n.prev is not None:
            n.prev.next = n.next
        if n.next is not None:
            n.next.prev = n.prev

        n.next = self.head
        if self.head is not None:
            self.head.prev = n
        n.prev = None
        self.head = n
