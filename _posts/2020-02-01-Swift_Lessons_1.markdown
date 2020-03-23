---
layout:     post
title:      "Swift_Lessons_1"
subtitle:   " \"利用Google Spreadsheet JSON & Imgur 開發App (1)\""
date:       2020-02-01 16:00:00
author:     "hon20002000"
header-img: "img/Python.png"
catalog: true
tags:
    - Swift
---

## 前言
  
'''  
作者: hon20002000   
最後更新: 2020/02/01    
'''   
  
本教程copy自(https://ccng830.github.io/2020/03/02/Google-Spreadsheet-JSON-&-imgur/) 
並加入一些圖片作補充.

>想更深入了解python, 網上資源可以看[廖雪峰的python教學網站](https://www.liaoxuefeng.com/wiki/1016959663602400)  
>或是[RUNOOB.com](http://www.runoob.com/python/python-tutorial.html)python教程
>教得十分仔細, 若想深入python的進階用法可以查看他們的內容   

教程用法:  
>>閱讀本blog上的基礎語法  
>>完成每篇文章的作業  
>>部分學習所需的檔案在[github](https://github.com/hon20002000/MacauAIChallenge2019_pythonLessons)下載  
>>遇到問題或其他改善建議可在下面留言


<p id = "build"></p>
---

## 正文

numpy和pandas module是機器學習必學的庫  
python內置的list功能很弱, 某些切片功能list是做不到的  
而numpy可以快捷地計算, 切片和reshape多維數組  
pandas在機器學習的使用較多, 它能輕易的組織及處理table類的表格(類似excel的功能)    
而在深度學習中則較少使用, 因為處理圖像不需這些功能, 因此pandas在深度學習中不是必須的   

    
   



return多個返回值     

    def calucale(x):
        y = 3*x + 4
        z = -2*x + 1
        return y, z

    result_1, result_2 = calucale(10)
    print("result_1:", result_1)   
    print("result_2:", result_2) 
    =========== result ==========
    result: 34
    result: -19
    
<p id = "build"></p>
---
    
## 練習


(a) 利用函數生成字典, 可以應用在生成機器學習的Label之中:  
    現在有3筆資料  
    - apple, 3個  
    - orange, 5個  
    - waterlemon, 10個  
    試用函數傳遞參數的方式生成字典fruits = {'apple':3, 'orange':5, 'waterlemon':10}, 例如  
    
    def make_fruit_dict(fruit_dt, fruit, num):
        ...etc


  
## 解答  

#(a)
  
    fruit_dict = {}
    def make_fruit_dict(fruit_dt, fruit, num):
        fruit_dt[fruit]=int(num)
        return fruit_dt
 
    make_fruit_dict(fruit_dict, 'apple', 3)  
    print("fruit_dict:", fruit_dict)  
    make_fruit_dict(fruit_dict, 'orange', 5)  
    print("fruit_dict:", fruit_dict)  
    make_fruit_dict(fruit_dict, 'waterlemon', 10)  
    print("fruit_dict:", fruit_dict)  
    =========== result ==========  
    fruit_dict: {'apple': 3}  
    fruit_dict: {'apple': 3, 'orange': 5}  
    fruit_dict: {'apple': 3, 'orange': 5, 'waterlemon': 10}  
  
#(b)  
  
    usernames_1 = ['John', 'Mary', 'Susan']  
    usernames_2 = ['John', 'Mary', 'Susan', 'tommy', 'Joan']  
  
    def print_user(users):  
        count = 0  
        for user in users:  
            print("user{}:".format(count), user)  
            count += 1  


    print_user(usernames_1)  
    print('-'*15)   
    print_user(usernames_2)  
    =========== result ==========    
    user0: John  
    user1: Mary  
    user2: Susan  
    ---------------  
    user0: John  
    user1: Mary  
    user2: Susan  
    user3: tommy  
    user4: Joan  
  
#(c)  
  
    def sum_ap(a1, d, n):    
        Sn = n*a1+n*(n-1)/2  
        an = a1 + (n-1)*d  
        return an, Sn  
  
    an, Sn = sum_ap(1,1,10)  
    print("an:",an)  
    print("Sn:",Sn)  
    =========== result ==========    
    an: 10  
    Sn: 55.0  
