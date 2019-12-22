class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.min = float('inf')


class Stack:
    # Last In First Out
    def __init__(self):
        self.head = None
        self.len = 0

    def push(self, data):
        node = Node(data)
        if self.head is None:
            self.head = node
            node.min = data

        else:
            node.next = self.head
            node.min = min(self.head.min, data)
            self.head = node


        self.len += 1
        print("Push:{}, len:{}".format(data, self.len))

    def pop(self):

        if self.len:
            out = self.head.data
            self.head = self.head.next
            self.len -= 1

        else:
            print("Nothing to pop")
            out =  None

        print("pop: {}".format(out))
        return out


    def isempty(self):
        if self.len:
            return False
        else:
            return True

    def peek(self):

        if self.len:

            out = self.head.data
        else:
           out = None

        print("peek:{}".format(out))
        return out

    def traverse(self):

        next_node = self.head
        print("traverse:")
        if not next_node:
            print("Stack empty currently")

        while next_node:
            print(next_node.data, "->", "min:{}".format(next_node.min))
            next_node = next_node.next

    def s_min(self):
        if self.len:
            out = self.head.min
        else:
            out = None

        print("min in stack: {}".format(out))
        return out


if __name__ == "__main__":
    s = Stack()
    s.push(5)
    s.push(3)
    s.push(2)
    s.push(4)

    s.peek()
    s.s_min()
    s.traverse()
    s.pop()
    s.traverse()
    s.pop()
    s.traverse()
    s.pop()
    s.traverse()
