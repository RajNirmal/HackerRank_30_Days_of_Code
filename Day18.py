import queue as q
class Stack:
    def __init__ (self):
        self.stacks = []
    def push(self,ch):
        self.stacks.append(ch)
    def pop(self):
        return self.stacks.pop()
        
class Solution:
    def __init__ (self):
        self.myStack = Stack()
        self.myQueue = q.Queue()
    def pushCharacter(self, ch):
        self.myStack.push(ch)
    def popCharacter(self):
        return self.myStack.pop()
    def enqueueCharacter(self,ch):
        self.myQueue.put(ch)
    def dequeueCharacter(self):
        return self.myQueue.get()