class MinStack:
    def __init__(self):
        #initialises the stack object
        self.stack = []
        self.min_stack = []

    def push(self, val: int) -> None:
        #pushes val to stack (append)
        self.stack.append(val)
        if not self.min_stack:
            self.min_stack.append(val)
        else:
            self.min_stack.append(min(val, self.min_stack[-1]))

    def pop(self) -> None:
        #normal pop - remove from top of stack
        self.stack.pop()
        self.min_stack.pop()

    def top(self) -> int:
        #return top of stack
        return self.stack[len(self.stack) - 1]

    def getMin(self) -> int:
        #return smallest element in stack
        return(self.min_stack[-1])
    
    
