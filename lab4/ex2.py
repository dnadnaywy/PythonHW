class Queue:
    queue = []

    def pop(self):
        if self.empty():
            return None

        element = self.queue[0]
        self.queue.remove(element)
        return element

    def push(self, element):
        self.queue.append(element)

    def peek(self):
        if self.empty():
            return None
        return self.queue[0]

    def empty(self) -> bool:
        if len(self.queue) == 0:
            return True
        return False


if __name__ == "__main__":
    queue = Queue()
    queue.push(21)
    print(queue.pop())
    print(queue.peek())
