---
layout:     post
title:      "MacauAIChallenge2019_Lessons_3"
subtitle:   " \"Ascii, unicode and utf-8\""
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

以下內容截取自[廖雪峰的python教學網站](https://www.liaoxuefeng.com/wiki/1016959663602400):  
  
字符串是一種數據類型, 由於計算機只能處理數字, 在處理文本需轉換為數字才能處理.  
  
計算機採用8bit(比特)作為1byte(字節)一所以1個byte最大的整數為255(11111111) 
  
如果要表示更大的整數, 則要用2個或更多的字節, 例如2個byte可表示65535(11111111 11111111)  
  
最早的ACSII編碼只能表示127個字符(即英文字和一些符號)(1byte)  
  
<img src="/img/ascii_1.gif" width="75%">  
<img src="/img/ascii_2.gif" width="75%">  
   
然後各國加入他們的文字, ACSII已經不夠編碼  
  
因此最終把所有語言統一到Unicode編碼(2byte)  
  
但是Unicode比ACSII使用多一倍儲存空間, 因此又產生了較為節省空間的可變長度編碼的uft-8  
   

<img src="/img/unicode.png" width="100%">  


一般的數據類型有:  
*    整數(int): -1, 0, 11, 100  
*    浮點數(float): 1.2, 3.33, 1.23e3(1.23x10^3)   
*    字符(char): 'a', 'b', "c"  
*    字符串(string): 'apple', "orange"  
*    布林值(boolean): 1, 0 , True, False  
*    空值(None): None(空集, None不是0)  
*    變量(Variable): filename, number, x, y  
  
        
常用運算符號及邏輯符號:  
- 加法(addition): +  
- 減法(Subtraction): -    
- 乘法(multiplication): *  
- 平方(square): **  
- 除法(division): /  
- 除法取整(division and Take the integer part): //  
- 餘數(remainder): %  
- 交集(Intersection): and   
- 並集(Union): or  
- 相等(equal): ==  
- 不相等(not equal): !=  
- 賦值(Assignment): =  
  

常用的functioin:   
- `print()`  #print出內容   
- `input()`  #輸入文字/數字, 輸出字串  
- `int()`    #把字串轉為整數
- `float()`  #把字串轉為浮點數
- `str()`    #把數值轉為字串
- `ord()`    #把ASCII轉為數字
- `type()`   #查詢變量類型  

<p id = "build"></p>
---

觀察一下整數的運算結果:

    a = 5
    b = 2
    print("a**b:", a**b)    
    print("a/b:", a/b)
    print("a//b:", a//b)
    print("a%b:", a%b)
    =========== result ==========
    a**b: 25
    a/b: 2.5
    a//b: 2
    a%b: 1

觀察一下字串的運算結果:

    a = 'apple'
    b = 'orange'  
    c = '121'
    d = '55'
    print("a+b:", a+b)    
    print("a*2:", a*2)  #通過簡單方法將字串double
    print("a, b:", a,    b)    #空格不影響結果
    print("a==b:", a == b)    
    print("a!=2:", a != b)
    print("int(c) - int(d):", int(c) - int(d)) 
    =========== result ==========
    a+b: appleorange
    a*2: appleapple
    a, b: apple orange
    a==b: False
    a!=b: True
    int(c) - int(d): 66
    
---

## HomeWork


下列寫法有什麼錯誤, 應該如何改才能得到正確答案?   

    ans=input()
    b = 25
    print("ans+b:", ans+b)  
    
下列結果是什麼?因此我們在做運算時要注意些什麼?  

    int_a = 13
    float_b = 13.55
    print("int_a//3:", int_a//3)
    print("int_a%3:", int_a%3)
    print("float_b//3:", float_b//3)
    print("float_b%3:", float_b%3)

下面的報錯是什麼意思?  

    a = '13'
    b = 13
    print("a**3:", a**3)

unsupported operand type(s) for ** or pow(): 'str' and 'int' 

    a = '13'
    b = 13
    print("a+b:", a+b)
    
must be str, not int  

    a = '13'
    b = 13
    print("b+a:", b+a)
    
unsupported operand type(s) for +: 'int' and 'str'  
