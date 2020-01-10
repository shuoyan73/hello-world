#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class MyStack:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.item=[]

    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        self.item.append(x)
        return

    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        j=len(self.item)-1
        d=self.item[j]
        self.item.pop()
        return d

    def top(self) -> int:
        """
        Get the top element.
        """
        j=len(self.item)-1
        W=self.item[j]
        return W
    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        if len(self.item)==0:
            return True
        else:
            return False
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()

