class Node:
    def __init__(self):
        self.prev: Node
        self.next: Node
        self.rectangle: int


class WinLL:
    def __init__(self):
        self.head = None

    def __iter__(self):
        current = self.head
        while current:
            yield current
            current = current.next

    def add_win(self):
        if self.head is None:
            self.head = Node()
            return self.head
        else:
            for win in self:
                pass
            win.next = Node()
            return win.next
