---
layout:     post
title:      "MacauAIChallenge2019_Lessons_4"
subtitle:   " \"List, for and slice\""
date:       2019-06-10 16:00:00
author:     "hon20002000"
header-img: "img/Python.png"
catalog: true
tags:
    - Python Quick start
---

## 前言

本教程是為了讓同學們快速體驗機器學習/深度學習而設計的.  
裡面只學習最常用的python語法.

>想更深入了解python, 網上資源可以看[廖雪峰的python教學網站](https://www.liaoxuefeng.com/wiki/1016959663602400)  
>>教得十分仔細, 若想深入python的進階用法可以查看他的內容   

教程用法:  
>>閱讀本blog上的基礎語法  
>>完成每篇文章的作業  
>>部分學習所需的檔案在[github](https://github.com/hon20002000/MacauAIChallenge2019_pythonLessons)下載  
>>遇到問題或其他改善建議可在下面留言


<p id = "build"></p>
---

## 正文

列表(list)一般用來儲存數據, 我們用中括號[ ]表示, 列表的重點在於可擴展性:  
列表的元素由0開始計算, 例如list[0]代表第1個元素, list[3]代表第4個元素  
list[-1]代表倒數第一個元素, list[-2]代表倒數第二個元素  
列表可用append()來加入新元素

    list_a = [1, 2.5, 'a', 'apple']
    list_a.append(4)
    print("list_a[4]:", list_a[4])    #原本沒有list_a[4]  
  
我們會說現在的list_a儲存了5個元素, 因此list_a的長度為5(我們用len()來求出list的元素個數)

    list_a = [1, 2.5, 'a', 'apple', 4]
    print("list_a:", list_a)
    print("len:", len(list_a))
    =========== result ==========
    list_a: [1, 2.5, 'a', 'apple', 4]
    len: 5
    
list其他的操作還有remove(), pop(), insert(),  sort(), sorted(), reverse(), del()等等  
而sum(list), max(list), min(list)等等可以對list內的元素作一個統計  

    list_a = [0, 1, 2, 3, 4]
    list_a.pop()
    print("list_a:", list_a)
    =========== result ==========
    list_a: [0, 1, 2, 3]
   
    list_a = [0, 1, 2, 3, 4]
    list_a.pop(2)
    print("list_a:", list_a)
    =========== result ==========
    list_a: [0, 1, 3, 4]

    list_a = [0, 1, 2, 3, 4]
    list_a.insert(2, 8)    #在2號位插入數字8
    print("list_a:", list_a)
    =========== result ==========
    list_a: [0, 1, 8, 2, 3, 4]

    list_a = [0, 1, 2, 4, 2]
    list_a.remove(2)    #remove第一個出現的2, 不會remove所有的2
    print("list_a:", list_a)
    =========== result ==========
    list_a: [0, 1, 3, 4]

    list_a = [3, 1, 5, 4, 2]
    list_a.sort()    #list_a永久改變
    print("list_a:", list_a)
    =========== result ==========
    list_a: [1, 2, 3, 4, 5]

    list_a = [3, 1, 5, 4, 2]
    list_a.reverse()    #list_a永久改變
    print("list_a:", list_a)
    =========== result ==========
    list_a: [5, 4, 3, 2, 1]
    
    list_a = [3, 1, 5, 4, 2]
    list_b = sorted(a)    #list_a不改變 
    list_c = sorted(a, reverse=True)    #list_a不改變 
    print("list_b:", list_b)
    print("list_c:", list_c)
    =========== result ==========
    list_b: [1, 2, 3, 4, 5]
    list_c: [5, 4, 3, 2, 1]
    
    list_a = [1, 2, 3, 4, 5]
    del list_a[3]    #list_a永久改變
    print("list_a:", list_a)
    =========== result ==========
    list_a: [1, 2, 3, 5]
<img src="/img/unicode.png" width="100%">  

<p id = "build"></p>
---

for可能是我們在python最先學到的一個重要關鍵字  
一般來說for是用來作迴圈, 使程序在循環中完成某些事  
以c++程序來說, for可以這樣使用:  

    for(int i=0; i<3; i++){     #第一次時i=0, 符合條件i<3, 因此i=i+1並且進入迴圈作某些功能
    ...                          #第二次時i=1, 餘此類推第4次時, i=3, 不符合條件i<3跳出迴圈, 由此控制進行3次迴圈
    }
    
在python中可以簡化寫成如下, 注意python不用寫{ }, 而是用縮進4個空格或1個tab來表示巢狀結構    

    for i in range(3):
        print("i:", i)
    =========== result ==========
    i: 0
    i: 1
    i: 2

也可以換個方式寫成  

    for i in range(0,3):
        print("i:", i)
    =========== result ==========
    i: 0
    i: 1
    i: 2

由此可知使用range()可以控制進行多少次迴圈, for和list可以組合一些用法

    list_a = []
    for i in range(1,4):
        list_a.append(i)
        print("list_a:", list_a)    #留意print()的位置
    =========== result ==========
    list_a: [1]
    list_a: [1, 2]
    list_a: [1, 2, 3]

    list_a = []
    for i in range(1,11):
        list_a.append(i**2)
    print("list_a:", list_a)    #留意print()的位置
    =========== result ==========
    list_a: [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

另外, 配合len()可以打印未知多少個元素的list, 便可以對裡面所有的元素進行操作

    list_a = [1, 2, 3, ..., 99, 100, ...]    #假設某未知數量的列表
    for i in range(len(list_a)):
        ...

for在python有一個特殊用法, 可以直接操作列表元素

    name_list = ['sam', 'john', 'monica']    
    for name in name_list:
        print("name:", name)
    =========== result ==========
    name: sam
    name: john
    name: monica

效果相當於:

    name_list = ['sam', 'john', 'monica']   
    for i in range(len(num_list)):
        print("name:", num_list[i])
    =========== result ==========
    name: sam
    name: john
    name: monica

---

切片(slice)在python當中特別重要, 切片表示使用list中的部分元素來操作

    name_list = [0, 1, 2, 3, 4, 5, 6]   
    print("name_list[:]:", name_list[:])
    print("name_list[1:4]:", name_list[0:4])
    print("name_list[:4]:", name_list[:4])
    =========== result ==========
    name_list[:]: [0, 1, 2, 3, 4, 5, 6]
    name_list[1:4]: [1, 2, 3]
    name_list[:4]: [0, 1, 2, 3]
    
二維列表(2-D list), 即是只有灰度(gray)的相片, 假設我要複制/切割4x5像素圖片中的左上角2x2區塊  
仔細觀察可發現應為[[1,2],[6,7]], 下面是實現方法

    img_data = [[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15],[16,17,18,19,20]]
    img_slice = img_data[:2]    
    print("img_slice:", img_slice)    #觀察img_slice是什麼
    save_img = [ ]    #建立空列表來儲存資料
    for img in img_slice:
        print("img:", img)    #觀察img是什麼
        save_img.append(img[:2])    #儲存資料
    print("save_img:", save_img)    #
    =========== result ==========
    img_slice: [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]]
    img: [1, 2, 3, 4, 5]
    img: [6, 7, 8, 9, 10]
    save_img: [[1, 2], [6, 7]]
    
    
## 練習


(a) 下列語法運行時出現錯誤:  
IndentationError: expected an indented blo  
要如何改才能印出數字呢?

    img_data = [1,2,3,4,5]
    for img in img_slice:
    print("img:", img)  

(b) 下列語法運行時出現錯誤:  
IndentationError: expected an indented block  
要如何改才能印出數字呢?

    img_data = [1,2,3,4,5]
    for img in img_slice
        print("img:", img)  
    =========== result ==========
            for img in img_slice
                                ^
    SyntaxError: invalid syntax
    
(c) 使用程序把數字1~100存進列表, print出此1~100個數字  
然後把1~100的數字相加後輸出結果(利用sum(list)), 然後從列表中利用切片抽出第40~50位的數字並相加 

(d) 複制列表時會出現一個bug, 改變複制列表會影響原列表, 如何避免?

    list_a = [1,2,3,4,5]
    list_b = list_a
    list_b.append(6)
    print("list_a:", list_a)
    print("list_b:", list_b)
    =========== result ==========
    list_a: [1,2,3,4,5,6]
    list_b: [1,2,3,4,5,6]

