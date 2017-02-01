class MinStack:
    # @param x, an integer
    def __init__(self):
        self.stack = []
        self.min_stack = []

    # # @return an integer
    # def push(self, x):
    #     self.stack.append(x)
    #     if len(self.min_stack) != 0 and x == self.min_stack[-1][0]:
    #         self.min_stack[-1] = (x, self.min_stack[-1][1] + 1)
    #     elif len(self.min_stack) == 0 or self.min_stack[-1][0] > x:
    #         self.min_stack.append((x, 1))

    # # @return nothing
    # def pop(self):
    #     if len(self.stack) != 0:
    #         if self.min_stack[-1][0] == self.stack[-1]:
    #             if self.min_stack[-1][1] > 1:
    #                 self.min_stack[-1] = (self.min_stack[-1][0], self.min_stack[-1][1] - 1)
    #             else:
    #                 self.min_stack.pop()
    #         self.stack.pop()

    # # @return an integer
    # def top(self):
    #     if len(self.stack) != 0:
    #         return self.stack[-1]
    #     return 0
        
    # # @return an integer
    # def getMin(self):
    #     if len(self.min_stack) != 0:
    #         return self.min_stack[-1][0]
    #     return 0

    # @return an integer
    def push(self, x):
        self.stack.append(x)
        if len(self.min_stack) == 0 or self.min_stack[-1] > x:
            self.min_stack.append(x)

    # @return nothing
    def pop(self):
        if len(self.stack):
            if len(self.min_stack) and self.min_stack[-1] == self.stack[-1]:
                self.min_stack.pop()
            self.stack.pop()

    # @return an integer
    def top(self):
        if len(self.stack) != 0:
            return self.stack[-1]
        
    # @return an integer
    def getMin(self):
        if len(self.min_stack) != 0:
            return self.min_stack[-1]



s = MinStack()
s.push(-1)
# s.push(1)
# s.push(4)

print s.stack
print s.min_stack
s.top()
# s.pop()
print s.getMin()