#!/usr/bin/env python
# coding: utf-8

# In[1]:


class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None
        
        """
        :type val: int
        :type next: ListNode
        :rtype: None        
        """
class MyHashSet:
    def __init__(self):
        self.capacity = 64
        self.data = [None] * 64
        
        """
        :type capacity: int
        :rtype: None
        """
        
    def add(self, key):
        """
        :type key: str
        :rtype: None
        """
        
        h=MD5.new()
        data=key
        h.update(data.encode('utf-8'))
      
        Key=(int(h.hexdigest(),16))
        
        i=Key%self.capacity
        #print(i)
        if self.data[i] is None:
            
                    
            self.data[i]=ListNode([key])
             
        else:
           
            
            node=self.data[i]
            while node:
                
                node=node.next
                
            else:
                node=ListNode([key])
                return
                 
               
                
                
    def remove(self, key):
        """
        :type key: str
        :rtype: None
        """
        
        h=MD5.new()
        data=key
        h.update(data.encode('utf-8'))
        
        Key=(int(h.hexdigest(),16))
        
        i=Key%self.capacity
      
         
        if self.data[i]:
            if self.data[i].val==[key]:
                self.data[i]=self.data[i].next
        else:
            node=self.data[i]
            while node.next:
                if node.next.val==[key]:
                    node.next=node.next.next
                    return
                node.next=node.next.next
            else:
                return
                    
             
      
    def contains(self, key):
        """
        :type key: str
        :rtype: bool(True or False)
        """
        h=MD5.new()
        data=key
        h.update(data.encode('utf-8'))
        
        Key=(int(h.hexdigest(),16))
        
        i=Key%self.capacity
        
        if self.data[i]:
            node=self.data[i]
            while node:
                
                if node.val==[key]:
                    
                    return True
                node=node.next
            else:
                return False
               
        else:
            return False


# In[ ]:




