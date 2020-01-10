#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.item=[]
        self.min=0
        self.tempmin=0
      
        
        
        

    def push(self, x: int) -> None:
        self.item.append(x)
        
        
        
            
            
            
        
        

    def pop(self) -> None:
        return self.item.pop()
        

    def top(self) -> int:
        return self.item[-1]

    def getMin(self) -> int:
        i=0
        for i in range(len(self.item)):
            i+=1
            self.min= min(self.item)
            return self.min
            
                
     


        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()

