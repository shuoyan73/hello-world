#!/usr/bin/env python
# coding: utf-8

# In[9]:


class Graph(): 

    def __init__(self, vertices): 
        self.V = vertices 
        self.graph = []
        self.graph_matrix = [[0 for column in range(vertices)]  
                    for row in range(vertices)] #用來建立圖(graph)
        self.root_finding=[-1 for column in range(vertices)]
        self.visited=[]
        self.distance=[]
        self.shortestpath={}
        self.Compare=[]
        self.k=[]
        self.weightlist=[]
        
        self.last={}
    def addEdge(self,u,v,w): 
       
        self.graph_matrix[u][v]=w
       
    def findroot(self,i):
        return i
    def Dijkstra(self, s): 
        
        
        ver_total=self.V
        
        while len(self.visited)!=ver_total:#當我的拜訪list與我全部頂點個數不同時：
           
            i=s#將匯入的起始點給i
            self.visited.append(i)#在拜訪list中增加該點
           
            for c in range(0,ver_total):#對所有頂點
                
                if len(self.distance)==ver_total:#如果存放距離list長度等於頂點個數（非第一次）
                    if c  in self.visited:#如果該頂點已經在拜訪過的list裡面，代表上個點可連接到他，且該distance最小
                        self.distance[c]=self.distance[c]#則維持原本距離
                        
                    else:#如果該頂點不在拜訪過的list裡面，則代表該位置距離並非最小距離，則要進行比較
                        
                        if self.distance[c]!=0 and self.graph[i][c]!=0:#如果該距離不為0（原本有且下個點有經過該點）
                            
                            if self.distance[c]>self.distance[i]+self.graph[i][c]:#如果 該原本距離加上下一個權重小於原本距離
                                self.distance[c]=self.distance[i]+self.graph[i][c]#則取代原本距離
                                
                            else:#如果 上個條件不成立，代表沒有更短，
                                self.distance[c]=self.distance[c]#則照舊
                        elif self.distance[c]!=0 and self.graph[i][c]==0:#如果該原本距離不為0但下個點沒有經過該點
                            self.distance[c]=self.distance[c]#則照舊
                            
                        elif self.distance[c]==0 and self.graph[i][c]!=0:#如果原本沒有且下個點有經過
                            
                            self.distance[c]=self.distance[i]+self.graph[i][c]#則取代原本距離
                        else:#原本沒有且下個點沒有經過
                            
                            self.distance[c]=self.distance[c]
                        
                else:#如果存放距離list長度等於頂點個數不成立（第一次）
                    
                    
                    
                    self.distance.append(self.graph[i][c])#將權重表中，頂點為i（橫列）對每個頂點(m直行)，加入到距離list裡面  
                    
                    
                #如果還有點沒有走訪，就要繼續找出下一個最小路徑之頂點 
            for k in range(0,ver_total):
                
                if k not in self.visited and self.distance[k]!=0:#如果該點未被走訪且該點權重不為0
                    #self.k.append(k)
                    self.Compare.append(self.distance[k])
                    
                    
                    
                if k==ver_total-1:
                    for t in range(0,ver_total):
                        if self.Compare:
                            if self.distance[t]==min(self.Compare):
                                Q=t
                                self.Compare=[]#結束之前清空給下一次用
                                #self.k=[]
                                return self.Dijkstra(Q)

        else:
            for e in range(0,ver_total):
                self.shortestpath.update({str(e):self.distance[e]})
            return self.shortestpath
        
    
    
    
    
    
    def Kruskal(self):
        
        
        C=[]
        var_total=self.V
        
        if self.weightlist==[]:
            for i in range(0,var_total):
                
                for j in range(0,var_total):
                    
                    if self.graph_matrix[i][j]!=0:
                        
                        
                        self.weightlist.append(self.graph_matrix[i][j])
                        self.weightlist.sort()
                        
                       
            if i==(var_total-1) and j==(var_total-1):
                
                while len(self.weightlist)!=len(C):
                    
                    for c in range(0,len(self.weightlist)):
                        
                        for i in range(0,var_total):
                            for j in range(0,var_total):
                                
                                if self.graph_matrix[i][j]==self.weightlist[c]:
                                    
                                    C.append(self.weightlist[c])
                                    
                                

                                    if self.root_finding[i]==-1 and self.root_finding[j]==-1:
                                        
                                        if self.root_finding[i]==self.root_finding[j]:
                                             
                                            self.root_finding[i]=j
                                            self.root_finding[j]=j
                                             
                                            self.last.update({str(i)+str('-')+str(j):self.graph_matrix[i][j]})
                                               
                                    elif self.root_finding[i]!=-1 and self.root_finding[j]==-1:
                                        
                                                
                                        self.root_finding[j]=self.root_finding[i]
                                           
                                        self.last.update({str(i)+str('-')+str(j):self.graph_matrix[i][j]})
                                         
                                    elif self.root_finding[i]==-1 and self.root_finding[j]!=-1:
                                        
                                            
                                        self.root_finding[i]=self.root_finding[j]
                                       
                                        self.last.update({str(i)+str('-')+str(j):self.graph_matrix[i][j]})
                                        
                                    elif self.root_finding[i]!=-1 and self.root_finding[j]!=-1:
                                        
                                        if self.root_finding[i]==self.root_finding[j]:
                                            self.root_finding[i]=self.root_finding[j]
                                            
                                        elif self.root_finding[i]!=self.root_finding[j]:
                                            R=self.root_finding[i]
                                          
                                            self.root_finding[i]=self.root_finding[j]
                                            
                                            for s in range(0,len(self.root_finding)):
                                                if self.root_finding[s]==R:
                                                    
                                                    self.root_finding[s]=self.root_finding[j]
                                                        
                                            self.last.update({str(i)+str('-')+str(j):self.graph_matrix[i][j]})
                                            
                                        
                                                                                   

                                        

                            
                        
                    else:
                        
                        return self.last
                     


                            


# In[ ]:




