class MinStack:

    def __init__(self):
        self.stack = []
        self.min_stack = []
        self.min_length = None

    def push(self, val: int) -> None:
        self.stack.append(val)
        if self.min_length == None:
            self.min_length = val
            self.min_stack.append(self.min_length)
        else:
            if val < self.min_length:
                self.min_length = val
            self.min_stack.append(self.min_length)
        


    def pop(self) -> None:
        if len(self.stack) == 0:
            return
        self.stack.pop()
        self.min_stack.pop()
        if len(self.min_stack) == 0:
            self.min_length = None
            return
        self.min_length = self.min_stack[-1]

    def top(self) -> int:
        if len(self.stack) == 0:
            return
        return self.stack[-1]

    def getMin(self) -> int:

        return self.min_length
        
