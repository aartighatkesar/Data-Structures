class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Queue:
    # First In First Out
    def __init__(self):
        self.head = None  # To de-queue
        self.rear = None  # To enqueue
        self.len = 0

    def enqueue(self, data):
        node = Node(data)
        if self.len == 0:
            self.head = node
            self.rear = node
        else:
            self.rear.next = node
            self.rear = node

        self.len += 1


    def dequeue(self):

        if self.len == 0:
            out = None
            print("Nothing to dequeue")

        else:
            out = self.head.data
            self.head = self.head.next
            self.len -= 1

        print("dequeue: {}".format(out))
        return out


    def peek(self):

        if self.len:
            out = self.head.data
        else:
            out = None

        print("Peek:{}".format(out))
        return out

    def traverse(self):

        node_next = self.head
        print("traverse")
        while node_next:
            print(node_next.data)
            node_next = node_next.next



if __name__ == "__main__":
    q = Queue()
    q.enqueue(2)
    q.enqueue(2)
    q.enqueue(4)
    q.enqueue(5)
    q.peek()
    q.traverse()
    q.dequeue()
    q.traverse()
    q.dequeue()
    q.traverse()

