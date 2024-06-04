from tkinter import Canvas, Event

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

    def add_win(self, new: Node):
        if self.head is None:
            self.head = new
        else:
            new.next = self.head
            self.head.prev = new
            self.head = new

        return self.head
