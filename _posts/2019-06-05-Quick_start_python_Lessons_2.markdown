---
layout:     post
title:      "Quick_start_python_Lessons_2"
subtitle:   " \"Ascii, unicode and utf-8\""
date:       2019-06-05 16:00:00
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

  
字符串是一種數據類型, 由於計算機只能處理數字, 在處理文本需轉換為數字才能處理.  
  
計算機其實經常默默的轉換編碼類型(例如讀取或儲存文件時)  
  
計算機採用8bit(比特)作為1byte(字節), 1個byte能表示最大的整數為255(11111111) 
  
你可以把1byte看作能對應255個不同符號, 那麼要表示世上所有不同的文字和符號, 肯定要更多的byte  
  
例如表示更大的整數, 則要用2個或更多的字節, 2個byte可表示65535(11111111 11111111)  
  
最早的ACSII編碼只能表示127個字符(即英文字和一些符號)(1byte)  
  
<img src="/img/ascii_1.gif" width="75%">  
<img src="/img/ascii_2.gif" width="75%">  
   
後來各國加入他們的文字, ACSII已經不夠編碼  
  
因此最終把所有語言統一到Unicode編碼(2byte)  
  
但是Unicode比ACSII使用多一倍儲存空間, 因此又產生了較為節省空間的可變長度編碼的uft-8  
   

<img src="/img/unicode2.png" width="100%">  

以上內容部分截取自[廖雪峰的python教學網站](https://www.liaoxuefeng.com/wiki/1016959663602400)    

<p id = "build"></p>
---

ord()是把字串轉換為數字, chr()是把數字轉換為字串  
觀察一下ord()和chr()的運算結果:

    print(ord('A'))
    print(chr(80))
    =========== result ==========
    65
    P


假設你現在用arduino讀取室內的溫度, 並用數據線或藍芽等返回數值回電腦  
  
那麼你直接讀取到的數據, 其實是b'27.7', 而不是'27.7'  
  
那麼b''是什麼意思呢, 又如何返回想要的數值(即27.7)?  
  
觀察一下encode()及decode()的運算結果:  

    print("i am a boy".encode('utf-8'))    #str類型通過encode轉為byte類型
    print(b'i am a boy'.decode('utf-8'))    #byte類型通過decode轉為str類型
    =========== result ==========
    b'i am a boy'
    i am a boy
    
由上面可知, 電腦在傳輸資料時會先將字串轉換為b'', byte(數字)  
我們可以通過python語法將byte轉回str或int來作進一步的處理  
  
  
  
最後, 我們學習如何在print()中的特定位置輸出數據:   
'%.nf'是指字串外面帶有%的數據(例如下面的3.1415926), 指定在''裡面的%數據在位置輸出  
%.2f是指只輸出小數後2位  
  
{}則比較簡較, 只要有{}的地方, 就可以按順序輸出答案  
  
    print('%.2f' % 3.1415926)    #%d表示輸出整數, %f表示輸出浮點數
    print("susan spent {:.1f} dollors, and john spent {} dollors.".format(1.5122,20))
    =========== result ==========
    3.14
    susan spent 1.5 dollors, and john spent 20 dollors.

---

## 練習


(a) k=3.1. b=2.6試計算直線方程y=kx+b, x=1.2時, y=?  
(1)以%的格式輸出答案  
(2)以{}及format()的格式輸出答案  
  
    
(b) 寫一個程序, 可以使用戶輸入名字和年齡, 輸出類似於  
My name is ____, I am ____ years ago.  

(c) 將下面於%.2f, {:.1f}.format()的裡的數字改寫, f改寫d, 看看結果  

    print('%.2f' % 3.1415926)    #%d表示輸出整數, %f表示輸出浮點數
    print("susan spent {:.1f} dollors, and john spent {} dollors.".format(1.5122,20))