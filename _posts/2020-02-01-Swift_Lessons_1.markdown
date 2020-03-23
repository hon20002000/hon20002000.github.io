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
  
本教程參考自(https://ccng830.github.io/2020/03/02/Google-Spreadsheet-JSON-&-imgur/)   
並加入一些圖片作補充.  


## 正文

開發iOS App時，我們都希望App內顯示的資料 (文字、數據、圖片等等)來自網絡上，因此更新數據就來得更加容易。  
而本文所介紹的方法適合單純地從網路抓資料顯示，不需要修改或上傳資料。  
我們需要利用網上的免費空間來儲存或讀取資料，例如表格資料及圖片。   
本範例使用Google Spreadsheet & imgur來儲存資料，我們一需要把表格資料轉換成 JSON 然後和 iOS App 串接。  

## 申請imgur的account  
  
首先利用imgur來上載一些圖片，目的是獲得圖片的url  
注意圖片的url是(https://i.imgur.com/rOFDO9i.jpg)  
而不是網站的url(https://hon20002000.imgur.com/all)  
在imgur注冊一個帳號，然後上傳圖片，最後點擊圖片copy url  
<img src="/img/1.gif" width="70%">  
  
## 建立Google Spreadsheet
  
搜尋Google Spreadsheet(Google 試算表)，即下面的link  
https://docs.google.com/spreadsheets/u/0/    
按右下角的按鈕，新增Spreadsheet  
  
<img src="/img/new_sheet.png" width="30%">    

輸入如下圖中的資料，copy圖片在 imgur的網址。   
注意儲存格中所有數據都必須是String格式，否則在Swift後面的處理會遇到麻煩。  
例如數字1在儲存格被定義為Int，而No.001則被定義為String，這是要注意的。  
<img src="/img/20200224.png" width="50%"> 
  
然後在google sheet的檔案按發佈到網路  
<img src="/img/20200224_1.png" width="50%">  
  
## 把google sheet的資料轉換成JSON的格式  
  
我們利用gsx2json把我們的google sheet轉換  
轉換方法是把下面網址上的xxxxx替換成你的id  

http://gsx2json.com/api?id=xxxxxxx&columns=false  

<img src="/img/link.png" width="100%">  
  
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
