#!/usr/bin/env python
# coding: utf-8

# # Heap sort 
# （製造成max heap 讓陣列由小到大排序）->
# 概念如下：
# 第一步是將陣列排序到完全二元樹裡面,因為要製造max heap所以
#     第二步是將每一個樹裡面左子樹和右子樹和該數的root比較,如果左子樹有大於該root的話,則左子樹換到root（因為要滿足父節點大於子節點的條件）,同理,如果右節點也大於root的話,那麼就將右子樹也換到root,然後再繼續向下處理,最後排序成一個max heap。 
# 接下來,把位在i=0（整個完全二元樹的root的節點移除並且將整個完全二元樹的最後一個節點的數字換到第一個節點（i=0)的位置,
#     然後,再持續利用原本的左子樹與右子樹和父節點比較的方式,將第二大的數字再移到整個完全二元樹的父節點的位置,依此類推,完成整個陣列有小到大的排序。
# 
# 
# 

# 由於定義right為arr[2*i+2]可能會超出list範圍,所以改成定義成index
# 我的想法是 先對所有的數字做heapify,再將index[0]的數字和index[最後]交換,接著在將剩下的二元樹進行heapify

# 先定義一個heapify的函數,顧名思義就是讓heap的父節點跟子節點比較,如果左子節點或著右子節點比父節點來的大的時候,將該節點和父節點交換。

# In[1]:


def Heapify(arr):
    for i in range(0,len(arr),1):
        root_large=
        left=2*i+1
        right=2*i+2
        if left<len(arr) and left>root_large:
            root_large=left
        if right<len(arr) and right>root_large:
            root_large=right


# In[ ]:


k=[2,5,3,6,7,3,4,2,1,9]


# 我的想法是從陣列的最後一個節點執行heapify到第一個節點，製造maxheap

# In[2]:


def heapify(A):
    
    for i in range (len(A)-1,-1,-1):#從9執行到1
        root=A[i]        
        l=2*i+1        
        r=2*i+2
        if l<len(A) and A[l]>A[i]:
            k=A[l]
            A[l]=A[i]
            A[i]=k
            
        if r<len(A) and A[r]>A[i]:
            k=A[r]
            A[r]=A[i]
            A[i]=k 
        if A[i]!=root:
            heapify(A)           
    return A
def heapsort(A):
    
    
    
    


# 假定一個Ａ陣列測試看看這個heapify的結果是什麼

# In[3]:


A=[3,4,9,2,7,1,6,5,8]


# In[4]:


hp=heapify


# In[5]:


hp(A)


# 結果發現,heapify後沒有每個父節點都大於子節點,所以應該要在增設一個條件,如果,i換成別的那麼要在執行一次heapify

# 這裏就是heapsort的部分了：
# 
# 我的想法是heapify之後要將index為0的節點和 最後一個節點交換,因為要排序成一個由小到大的陣列,所以要把heapify
# 過所形成的maxheap,index0的節點拉到陣列的最後面。將index0和最後一個節點位置互換之後,要再重新heapify一次,
# 因為已經不合maxheap的條件了。
# 所以,

# 從第０個執行到len(num)-i-1個 因為當第一次heapify 結束之後會將最後節點和第一節點互換,然後第一個節點的位置就已經
# 固定在最後一個了,然後互換完之後又要再做一次heapify,但是這時候就不用動到最後一個節點,所以我這邊設的len(arr)-i-1
# 就是每次heapify 結束後,就會將第一個和最後一個節點互換,然後要在執行第二次heapify的時候就i=1(len(arr)-1-1)
# 執行到倒數第一個，試試看這樣可否

# In[6]:


class Solution(object):     
    def heap_sort(self,num:int):
        
        for i in range(0,len(num)-1,1):
            for i in range (0,len(num)-i-1,1):
                root=num[i]
                l=2*i+1
                r=2*i+2
                
                if l<len(num) and num[l]>num[i]:
                    k=num[l]
                    num[l]=num[i]
                    num[i]=k
            
            
                if r<len(num) and num[r]>num[i]:
                    k=num[r]
                    num[r]=num[i]
                    num[i]=k 
                if num[i]!=root:
                    heap_sort(num)
                
                k=num[len(num)-1]
                num[len(num)-1]=num[0]
                num[0]=k
        return num        
        
         
        


# In[7]:


num=[4,-2,-4,3,5,1,7,3,-8]


# 執行後出現錯誤,指出在for迴圈的地方,因為i為區域變數

# In[9]:


Solution().heap_sort(num)


# In[10]:


class Solution(object):     
    def heap_sort(self,num:int):
        
        for i in range(0,len(num)-1,1):
            for i in range (0,len(num)-i-1,1):
                root=num[i]
                l=2*i+1
                r=2*i+2
                
                if l<len(num) and num[l]>num[i]:
                    k=num[l]
                    num[l]=num[i]
                    num[i]=k
            
            
                if r<len(num) and num[r]>num[i]:
                    k=num[r]
                    num[r]=num[i]
                    num[i]=k 
                if num[i]!=root:
                    heap_sort(self,num)
                
                k=num[len(num)-1]
                num[len(num)-1]=num[0]
                num[0]=k
        return num      


# 出現錯誤,heap_sort無法在運行時使用所以我覺得應該要將heapify先寫出來,在利用heap＿sort,去呼叫heapify
# 所以我改寫heap_sort了,現在我要做的是將做完的maxheap的父節點index0跟最後一個節點交換位置index(len(num)-1)
# 目前寫的邏輯是：
# 從第0個執行到第(num長度-1)次,每次將heap第0個節點匯入到m當中,然後再將最後一個節點匯入到第0個位置,
# 再將剛剛匯入到m的第0個節點的值拉出來放到最後一個位置,最後要將長度扣掉1,因為當我把maxheap裡面最大值放到最後一個節點的時候，
# 該節點也等於排序完成。

# when you first time run this loop use len(nums) to be the first L after that minus one each time

# In[11]:


class Solution(object):
   
    def heapify(self,nums):
        if not nums:
            return none
        else:
            L=len(nums)#the length of the list 
            L-=1
            for j in range(0,2,1):#2 times heapify
                for i in range(0,L,1):# i=0,1,2,...,L-1
                    root=i          
                    l=2*i+1
                    r=2*i+2    
                    if l<L and nums[l]>nums[i]:
                        P=nums[root]
                        nums[root]=nums[l]
                        nums[l]=P
                    if r<L and nums[r]>nums[i]:
                        Q=nums[root]
                        nums[root]=nums[r]
                        nums[r]=Q
            #update new list length by  minus one each time 
            print(nums) #print the list after heapify twice 
    def  heap_sort(self,nums):
        L=len(nums)
                             
        for k in range(0,L,1):       #k=0,1,...,L-1
            self.heapify(nums)   #heapify and print the list after heapify twice
            print(k)     # print k each time in order to see the changes
            if len(nums)<0:
                return nums[0] 
            else:
                print('heapify結束要swap:'+'nums')
                print(nums)
                        #k=0 L=L/k=1 L=L-1 / k=2 L=L-2/..
                m=nums[0]     #zero index value into m 
                nums[0]=nums[L-1]   #zero index=last index value
                nums[L-1]=m#put zero index value into lastnode
                print(nums)
                print(L)#show len(nums)
                


# In[12]:


K=[2,-1,3,6,9,7,-3,-4,-6,4,1]


# In[13]:


P=[2,3,1,6,-1]


# In[14]:


S=Solution()


# In[15]:


S.heap_sort(P)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




