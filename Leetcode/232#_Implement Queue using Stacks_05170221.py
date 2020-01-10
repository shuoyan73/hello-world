#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.item=[]
        #self.topnode=self.item[0]
        #self.backnode=self.item[]

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        self.item.append(x)
        return

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        k=self.item[0]
        self.item.pop(0)
        return k

    def peek(self) -> int:
        """
        Get the front element.
        """
        R=self.item[0]
        return R

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        if len(self.item)==0:
            return True
        else:
            return False


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()

