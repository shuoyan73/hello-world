#!/usr/bin/env python
# coding: utf-8

# In[10]:


class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None
        
class MyHashSet:
    def __init__(self,capacity=5):
        self.capacity = capacity
        self.data = [None] * capacity
        
       
        
    def add(self, key):
       
        from Crypto.Hash import MD5
        h=MD5.new()
        data=key
        h.update(data.encode('utf-8'))
      
        Key=(int(h.hexdigest(),16))
        
        i=Key%self.capacity
        
        if self.data[i] is None:
            
                    
            self.data[i]=ListNode(Key)
            return 
             
        else:
           
            
            node=self.data[i]
            while node:
                
                node=node.next
                
            else:
                node=ListNode(Key)
                return
                 
               
                
                
    def remove(self, key):
        
        from Crypto.Hash import MD5
        h=MD5.new()
        data=key
        h.update(data.encode('utf-8'))
        
        Key=(int(h.hexdigest(),16))
        
        i=Key%self.capacity
      
         
        if self.data[i]:
            if self.data[i].val==Key:
                self.data[i]=self.data[i].next
                return
            else:
                node=self.data[i]
                while node.next:
                    if node.next.val==Key:
                        node.next=node.next.next
                        return
                    node.next=node.next.next
                else:
                    return
        else:
            return
             
      
    def contains(self, key):
        from Crypto.Hash import MD5
        h=MD5.new()
        data=key
        h.update(data.encode('utf-8'))
        
        Key=(int(h.hexdigest(),16))
        
        i=Key%self.capacity
        
        if self.data[i]:
            node=self.data[i]
            while node:
                
                if node.val==Key:
                    
                    return True
                node=node.next
            else:
                return False
               
        else:
            return False
     
        

