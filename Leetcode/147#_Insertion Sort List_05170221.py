#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        #First  Step:檢查是否有head＆head.next 兩者缺一則回傳 head 
        if not head or not head.next: return head
        #Second Step:兩者都有則執行下面code 
        out = head #第一個節點的值 先匯到out(sorted output list)
        head = head.next #第二個節點先變成head
        tail = out #第一個節點?
        while head:#遇到head 要執行的動作（第二個節點的值與第一個節點的值比較）
            temp = head #第二個節點的值 先匯到 temp
            head = head.next#第三個節點的值
            if temp.val <= out.val:#如果第二個節點的值小於等於第一個節點的值
                temp.next = out 
                #第二個節點的next就會指向第一個節點,等於將第一個節點往後移一個位置
                out = temp #將第二個節點匯到out（sorted output list)裡面 
            elif temp.val >= tail.val: #如果第二個節點的值大於等於第一個節點 
                tail.next = temp #第一個節點的next就會指向第二個節點
                tail = temp #將第二個節點匯到tail中
            else:             #全部分完狀況？
                it = out         # 將out(sorted output list) 匯到it
                while it.next != tail and it.next.val < temp.val: #
                    it = it.next
                temp.next = it.next
                it.next = temp
        tail.next = None
        return out                   #(sorted output list)


# In[ ]:




