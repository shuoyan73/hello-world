#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class TreeNode(object):
    def __init__(self,x):
        self.val=x                        
        self.left=None                    
        self.right=None                  
    def insert(self,root,val):
        if self.val>=val:
            if self.left and self.left.val!=None:
                
                
                return self.left.insert(root,val)
            else:
                self.left=TreeNode(val)
                return self.left
        if self.val<val:
            if self.right and self.right.val!=None:
        
                
                return self.right.insert(root,val)
            else:
                self.right=TreeNode(val)
                return self.right
    def search(self,root,target):
        
        if self.val>target:
            if self.left.val!=None:
                
                if self.left.val==target:
                   
                    return self.left
                else:
                
                    return self.left.search(root,target)  
            else:
                
                return None
        elif self.val<target:
            
            
            
            if self.right.val!=None:
                
                if self.right.val==target:
                    
                    return self.right
                else:
                     return  self.right.search(root,target)
            else:
                return None
        elif self.val==target:
            return self
        
        
    def delete(self,root,target):
        self.root=root
        if self:#3
            
            if self.val<target:
                if self.right:
                    return self.right.delete(root,target)
            elif self.val>target:
                if self.left:
                    
                    return self.left.delete(root,target)
            elif self.val==target:
                if self.left and self.right:
                    if self.right:
                        temp=self.right
                        while temp.left!=None:
                            temp=temp.left
                        self.val=temp.val
                        temp.val=None
                        
                        return self.root
                        
                elif self.left or self.right:  
                    if self.left!=None:
                        
                        
                        if self.val==self.left.val:
                            return self.left.delete(root,target)
                        else:
                            self.val=self.left.val 
                            self.left.val=None
                            
                            self.root=root
                            return self.root
            
                    elif self.right!=None:
                        if self.val==self.left.val:
                            return self.left.delete(root,target)
                        else:
                            self=self.right
                            self.right=None
                            
                            return self.root
                            
                elif not self.left and not self.right:
                    self.val=None
                    
                    return self.root
                        
        else:
            return None
    
            
    
            
    
            
        
                
class Solution(object):
    def __init__(self):                    
        self.root=None
        
    def insert(self,root,val):                    
        self.root=root
        if self.root.val!=None:
            if self.root.val>=val:
                if self.root.left:
                    return self.root.left.insert(root,val)
                else:
                    
                    self.root.left=TreeNode(val)
                    return self.root.left
            elif self.root.val<val:
                if self.root.right:
                    return self.root.right.insert(root,val)
                    
                else:
        
                    self.root.right=TreeNode(val)
                    return self.root.right
        else:
            self.root=TreeNode(val)
            return self.root
            
    def delete(self,root,target):
        self.root=root
        
        if self.root!=None:
          
            if self.root.val<target:
                if self.root.right!=None:
                    return self.root.right.delete(root,target)
                else:
                    pass
                               
            elif self.root.val>target:
                if self.root.left!=None:
                    return self.root.left.delete(root,target)
                else:
                    pass
            elif self.root.val==target:
                if self.root.left and self.root.right:
                    
                    if self.root.right:
                        temp=self.root.right
                        while temp.left!=None:
                            temp=temp.left
                        self.val=temp.val
                        temp=None
                        
                        return self.root
                        
                elif self.root.left or self.root.right:
                    if self.root.left:
                        if self.root.val==self.root.left.val:
                            return self.root.left.delete(root,target)
                        else:
                            self.root=self.root.left
                            
                            self.root.left=None
                            
                            self.root=root
                            return self.root
                    if self.root.right:
                        if self.root.val==self.root.right.val:
                            return self.root.right.delete(root,target)
                        else:
                            self.root=self.root.right
                            self.root.right=None
                            
                            return self.root
                elif not self.root.left and not self.root.right:
                    
                    self.root=None
                    
                    return self.root
                
        else:
            return None
                            
 ############################SEARCH#####################################################     
    def search(self,root,target):
        self.root=root
        if self.root:
            if (self.root.val==target):
                return self.root
            else:
                if self.root.val>target:
                    if self.root.left:
                        if (self.root.left.val==target):
                            return self.root.left
                        else:
                            return self.root.left.search(root,target)
                            
                    else:
                        return None
                elif self.root.val<target:
                    if self.root.right:
                        
                        if (self.root.right.val==target):
                            return self.root.right
                        else:
                            return self.root.right.search(root,target)
                        
                    else:
                        return None
               
                        
            
        else:
            
            return None
    def modify(self, root, target, new_val):
        self.root=root
        if self.root:
            if self.root.val<target:
                self.root.right.delete(root,target)
                if self.root.val<new_val:
                    return self.root.right.insert(root,new_val)
                elif self.root.val>=new_val:
                    return self.root.left.insert(root,new_val)

            elif self.root.val>target:
                self.root.left.delete(root,target)
                if self.root.val<new_val:
                    return self.root.right.insert(root,new_val)
                elif self.root.val>=new_val:
                    return self.root.left.insert(root,new_val)
                    
            elif self.root.val==target:
                self.root.delete(root,target)
                if self.root.val<new_val:
                    return self.root.right.insert(root,new_val)
                elif self.root.val>=new_val:
                    return self.root.left.insert(root,new_val)
        else:
            return None
            

