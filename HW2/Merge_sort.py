#!/usr/bin/env python
# coding: utf-8

# # mergesort(合併排序）
# 將資料不斷分成兩半,直到資料只剩下一個節點,接下來兩兩排序，小的放前面,大的放後面,接下來合併起來,最後變成一個由小到大的序列。
# 因為觀察到每次做的事：1.分成左右兩陣列->2.左右兩陣列比較大小->3.左右兩陣列合併 
# 時間複雜度是O(nlogn)
# 1.以陣列長度為主,(將開頭到陣列長度一半分成左半,陣列長度一半到結束分成右半)->(左半再分成各半,右半再分成各半)->(分到剩下一個節點)
# ,總共:len(A)-1次  
# 2.
#   

# In[ ]:


class Solution(object):
    def merge_sort(self,nums):
        #divide into one element in  each array
        #compare Left&Right
        #merge two array


# 定義->寫演算法   先判斷有沒有這個東西 左邊的節點和右邊節點比較大小,小的先放

# In[23]:


class Solution(object):
    def merge_sort(self,nums):
        if len(nums)>1:                   
            mid=len(nums)//2
            left_array=nums[:mid]
            right_array=nums[mid:]
            self.merge_sort(left_array)
            self.merge_sort(right_array)
            
            left=0
            right=0
            merged=0
            while left<len(left_array) and right<len(right_array):
                if left_array[left]<right_array[right]:
                    nums[merged]=left_array[left]
                    left=left+1
                    merged+=1
    
                else:
                    right_array[right]<left_array[left]
                    nums[merged]=right_array[right]
                    right=right+1
                    merged+=1
                
            while left<len(left_array):
                nums[merged]=left_array[left]
                left+=1
                merged+=1
            while right<len(right_array):
                nums[merged]=right_array[right]
                right+=1
                merged+=1
                
        nums
        print(nums)
                
            
                
                    
            
        


# In[24]:


M=[9,3,1,4,2,6,8,7,0,1]


# In[25]:


W=Solution()
W.merge_sort(M)


# 現在我要改成只要print最後一次排序好的完整陣列,前面的每一次排序好的不需要print,如果我把mergesort(left_array)改成合併在left_array裡面
# merge_sort(right_array)也是,最後在印出left_array+right_array,發現不太可行,因為如果我這樣改,會跟我的原本在比較的left_array搞混，
# 所以我在想是不是要改成匯入到一個暫存的陣列裡面？放到暫存陣列的結果仍然不能,我現在要把第一次執行的陣列長度放到陣列裡面,第二次執行的時候,
# 設立一個if條件判斷,是否長度和第一次存放的長度一樣,區分第一次第二次,因為第一次存是為了要在最後進行判斷 如果陣列長度跟第一次存訪的依樣的話在印出來就好
