#!/usr/bin/env python
# coding: utf-8

# In[6]:



from collections import defaultdict 
  

class Graph:
    
    def __init__(self): 
        
        self.graph = defaultdict(list)
        self.queue1=[]
        self.queue2=[]
        self.stack1=[]
        self.stack2=[]
        

    
    def addEdge(self,u,v): 
        self.graph[u].append(v) 
        
   
  
    
    def BFS(self, s): 
        
        
        if len(self.graph)!=len(self.queue2):
            
            if not self.queue1 and not self.queue2:
                self.queue2.append(s)
                for i in self.graph[s]:
                    if i not in self.queue1:
                        if i not in self.queue2:
                            self.queue1.append(i)
                            
                
                
                self.queue2.append(self.queue1[0])
                
                k=self.queue1[0]
                
                self.queue1.pop(0)
                
                return self.BFS(k)         
               
                
               

            else:
                
                
                for i in self.graph[s]:
                    if i not in self.queue1:
                        if i not in self.queue2:
                            
                            self.queue1.append(i)
                
                self.queue2.append(self.queue1[0])
                k=self.queue1[0]
                self.queue1.pop(0)
                return self.BFS(k)
                
        else:
            
            return self.queue2
    def DFS(self, s):
        
        if len(self.graph)!=len(self.stack2):
            
            if not self.stack1 and not self.stack2:
                
                self.stack2.append(s)
                for i in self.graph[s]:
                    if i not in self.stack1:
                        if i not in self.stack2:
                            self.stack1.append(i)
                x=len(self.stack1)-1
                k=self.stack1[x]
                self.stack2.append(k)
                self.stack1.pop()
                return self.DFS(k)
            else:
                
                for i in self.graph[s]:
                    if i not in self.stack1:
                        if i not in self.stack2:
                            self.stack1.append(i)
                x=len(self.stack1)-1
                k=self.stack1[x]
                
                self.stack2.append(k)
                self.stack1.pop()
                return self.DFS(k)
        else:
            return self.stack2
        


# In[ ]:




