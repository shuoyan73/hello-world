#!/usr/bin/env python
# coding: utf-8

# In[1]:


#定義一個函數為quicksort
def quicksort(data):
    data_L=[]
    data_R=[]
    data_pivot=[]
    if not data :return data                  #如果data是none則回傳 data
    else:                                     #如果data不是None就執行這堆指令
                                              #指定data最後一個index是end
        pivot=data[len(data)-1]              #將data最後一個節點設為pivot(pivot要和pivot以外其他節點比較大小)
                                         
        for j in range(0,len(data),1):        #從陣列data的index(0)到index(倒數第一個)執行下面這堆指令,每次增加1
            if data[j]<pivot:                 #如果data[j]小於pivot
                                              #將data[j]的值匯入到data_L的陣列裡面
                data_L.append(data[j])            
                
            elif data[j]>pivot:              #如果陣列data[j]大於pivot
                data_R.append(data[j])       #將data[j]匯入到data_R的陣列裡面
            else:                            #和pivot相等和pivot本身匯入到data_pivot陣列
                data_pivot.append(pivot)
    data_L=quicksort(data_L)                 #更新data_L＝呼叫quicksort 函數再將pivot左邊陣列依照上面指令排列一次
    data_R=quicksort(data_R)                 #更新data_R＝呼叫quicksort 函數再將pivot左邊陣列依照上面指令排列一次
    return data_L+data_pivot+data_R          #回傳 data_L加上data_pivot加上data_R
        


# In[2]:


data=[1,3,2,5,1,3,4]


# In[3]:


quicksort(data)


# In[ ]:




