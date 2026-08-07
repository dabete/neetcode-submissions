class MinStack:

    def __init__(self):
        self.stack = []
        self.smallest_number = []
        

    def push(self, val: int) -> None:
        self.stack.append(val)
        if len(self.smallest_number) == 0:
            self.smallest_number.append(val)
        elif self.smallest_number[-1] >= val:
            self.smallest_number.append(val)
        

    def pop(self) -> None:
        value_popped = self.stack.pop()
        if value_popped == self.smallest_number[-1]:
            self.smallest_number.pop()


    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.smallest_number[-1]
        
