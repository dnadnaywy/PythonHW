class Stack:
    stack = []

    def pop(self):
        if self.empty():
            return None

        element = self.stack[len(self.stack) - 1]
        self.stack.remove(element)
        return element


    def push(self, element):
        self.stack.append(element)


    def peek(self):
        if self.empty():
            return None

        element = self.stack[len(self.stack) - 1]
        return element

    def empty(self) -> bool:
        if len(self.stack) == 0:
            return True
        return False

if __name__ == "__main__":
    stack = Stack()
    stack.push(21)
    print(stack.peek())
    print(stack.pop())
