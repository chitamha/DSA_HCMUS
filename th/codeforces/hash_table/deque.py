import sys

write = sys.stdout.write

class Node:
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None

class Deque:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def push_front(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    def push_back(self, value):
        new_node = Node(value)
        if self.tail is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node

    def pop_front(self):
        if self.head is None:
            return None
        value = self.head.value
        self.head = self.head.next
        if self.head is not None:
            self.head.prev = None
        else:
            self.tail = None
        return value

    def pop_back(self):
        if self.tail is None:
            return None
        value = self.tail.value
        self.tail = self.tail.prev
        if self.tail is not None:
            self.tail.next = None
        else:
            self.head = None
        return value
    
    def get(self, index):
        cur_node = self.head
        for _ in range(index):
            if cur_node is None:
                return None
            cur_node = cur_node.next
        return cur_node.value if cur_node is not None else None
    
def main():
    q = int(input())
    deque = Deque()
    for _ in range(q):
        command = input().split()
        if command[0] == '1':
            deque.push_back(int(command[1]))
        elif command[0] == '2':
            deque.push_front(int(command[1]))
        elif command[0] == '3':
            write(f"{deque.pop_back()}\n")
        elif command[0] == '4':
            write(f"{deque.pop_front()}\n")
        elif command[0] == '5':
            write(f"{deque.get(int(command[1]))}\n")

if __name__ == "__main__":
    main()