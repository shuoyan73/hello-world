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
            if self.left:
                self.left.insert(root,val)
            else:
                self.left=TreeNode(val)
        if self.val<val:
            if self.right:
                self.right.insert(root,val)
            else:
                self.right=TreeNode(val)
    def search(self,root,target):
        print(self.val)
        if self.val>target:
            if self.left:
                
                if self.left.val==target:
                   
                    return self.left.val
                else:
                    
                    self.left.search(root,target)  
            else:
                
                return None
        elif self.val<target:
            print(self.val<target)
            
            
            if self.right:
                
                if self.right.val==target:
                    
                    return self.right.val
                else:
                    self.right.search(root,target)
            else:
                return None
        elif self.val==target:
            return self.val
        
        
    def delete(self,root,target):
        
        if self:
            
            if self.val<target:
                if self.right:
                    self.right.delete(root,target)
            elif self.val>target:
                if self.left:
                    self.left.delete(root,target)
            elif self.val==target:
                if self.left and self.right:
                    if self.right:
                        if not self.right.left:
                            self.val=self.right.val
                            self.right.delete(root,target)
                        else:
                            if self.right.left:
                                if self.right.left.left:
                                    if self.right.left.left.left:
                                        if self.right.left.left.left.left:
                                            pass
                                        else:
                                            self.val=self.right.left.left.left.val
                                            self.right.left.left.left.delete(root,target)
                        
                elif self.left or self.right:  
                    if self.left:
                        self.val=self.left.val
                        if self.left.left:
                            self.left.val=self.left.left.val
                            if not self.left.left.left:
                                self.left.left.val=None
                            
            
                    if self.right:
                        self.val=self.right.val
                        if self.right.right:
                            self.right.val=self.right.right.val
                            if not self.right.right.right:
                                self.right.right.val=None
                            
                elif not self.left and not self.right:
                    self.val=None
                        
        else:
            return None
            
       
            
    
            
        
                
class Solution(object):
    def __init__(self):                    
        self.root=None
        
    def insert(self,root,val):                    
        self.root=root
        if self.root:
            if self.root.val>=val:
                if self.root.left:
                    self.root.left.insert(root,val)
                else:
                    self.root.left=TreeNode(val)
            elif self.root.val<val:
                if self.root.right:
                    self.root.right.insert(root,val)
                else:
                    self.root.right=TreeNode(val)
        else:
            self.root=TreeNode(val)
            
    def delete(self,root,target):
        self.root=root
        if self.root:
            if self.root.val<target:
                if self.root.right:
                    return self.root.right.delete(root,target)
                else:
                    return None             
            elif self.root.val>target:
                if self.root.left:
                    return self.root.left.delete(root,target)
                else:
                    return None
            elif self.root.val==target:
                if self.root.left and self.root.right:
                    
                    if self.root.right:
                        if not self.root.right.left:
                            self.root.val=self.root.right.val
                            self.root.right.delete(root,target)
                            return self.root.val
                        else:
                            if self.root.right.left:
                                if self.root.right.left.left:
                                    if self.root.right.left.left.left:
                                        pass
                                    else:
                                        self.root.val=self.root.right.left.left.val
                                        self.root.right.left.left.delete(root,target)
                            
                elif self.root.left or self.root.right:
                    if self.root.left:
                        self.root.val=self.root.left.val
                        self.root.left.delete(root,target)
                    if self.root.right:
                        self.root.val=self.root.right.val
                        self.root.right.delete(root,target)
                elif not self.root.left and not self.root.right:
                    
                    self.root.val=None
                
        else:
            return None
                            
 ############################SEARCH#####################################################     
    def search(self,root,target):
        self.root=root
        if self.root:
            if (self.root.val==target):
                return self.root.val
            else:
                if self.root.val>target:
                    if self.root.left:
                        if (self.root.left.val==target):
                            return self.root.left.val
                        else:
                            return self.root.left.search(root,target)
                            
                    else:
                        return None
                elif self.root.val<target:
                    if self.root.right:
                        
                        if (self.root.right.val==target):
                            return self.root.right.val
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
                    self.root.right.insert(root,new_val)
                elif self.root.val>=new_val:
                    self.root.left.insert(root,new_val)

            elif self.root.val>target:
                self.root.left.delete(root,target)
                if self.root.val<new_val:
                    self.root.right.insert(root,new_val)
                elif self.root.val>=new_val:
                    self.root.left.insert(root,new_val)
                    
            elif self.root.val==target:
                self.root.delete(root,target)
                if self.root.val<new_val:
                    self.root.right.insert(root,new_val)
                elif self.root.val>=new_val:
                    self.root.left.insert(root,new_val)
        else:
            return None
            
        
        
        
        
        
        
        
        
        
        
        
        

