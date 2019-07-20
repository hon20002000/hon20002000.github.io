---
layout:     post
title:      "MacauAIChallenge2019_Lessons_1"
subtitle:   " \"Intrduction of machine/deep learning\""
date:       2019-07-01 16:00:00
author:     "hon20002000"
header-img: "img/Python.png"
catalog: true
tags:
    - Machine/Deep Learning Quick start
---

## 前言
    
本教程是為了讓同學們快速體驗機器學習/深度學習而設計的.  
裡面只學習最常用的python語法.  
  
教程用法:  
>>閱讀本blog上的基礎語法  
>>完成每篇文章的作業  
>>部分學習所需的檔案在[github](https://github.com/hon20002000/MacauAIChallenge2019_pythonLessons)下載  
>>遇到問題或其他改善建議可在下面留言

<p id = "build"></p>
---

## 正文

我們的目標是訓練一個能辨認120種交通標誌的程序  
我們可以使用機器學習/深度學習的工具來完成它:  
>主要步驟為:  
>(1)收集資料(拍照收集圖片, 平均每種圖片約200-500張)  
>(2)把圖片分類並標記名稱(每種標誌建立file, 根據名稱存放相應的圖片)  
><img src="/img/turnRight.png" width="40%">  
>(3)編寫程序讀取圖片的資料, 並和標籤建立一一對應關係  
><img src="/img/label2.png">  
>(4)編寫機器/深度學習系統  
>(5)利用圖片資料和對應的標籤訓練學習系統  
>(6)學習系統會對每張圖片給出答案, 和預設的標籤相比較, 得出系統的準確率  
>(7)改善學習系統以獲得更高的準確率  
  
詳情參閱下面網址:  
[MacauAIChallenge2019_pythonLessons](https://github.com/hon20002000/MacauAIChallenge2019_pythonLessons)  

## 練習
  
(1)什麼是監督式學習(Supervised learning)?  
(2)什麼是神經網絡(neural network)?  
(3)什麼是深度學習(deep learning)?  
(4)mnist數據集是什麼, 用什麼方法完成分類? 
(5)carfi10數據集是什麼, 用什麼方法完成分類? 

---


