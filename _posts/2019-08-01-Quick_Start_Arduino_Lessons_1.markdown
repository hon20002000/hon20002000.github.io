---
layout:     post
title:      "Quick_Start_Arduino_Lessons_1"
subtitle:   " \"Introducation of Arduino\""
date:       2019-08-01 16:00:00
author:     "hon20002000"
header-img: "img/Python.png"
catalog: true
tags:
    - Quick Start Arduino
---
## 前言
  
'''  
作者: hon20002000   
最後更新: 2019/9/23  
'''   
  
本教程是為了讓同學們快速學習Arduino, 開發物聯網應用而設計的.  
裡面只學習最常用的Arduino語法.主要簡介
- 常用開發板的介紹
- 基本語法
- 常見sensor的原理及編程
- 藍牙應用
- wifi應用
- 物聯網應用

>由於arduino的入門教程實在太多    
>因此這裡就不再重新寫作一份教程了     
>這裡簡單介紹一下arduino自學中的重點以及特別要注意的地方     
>>網上資源可以看  
>>[W3Cschool](https://www.w3cschool.cn/arduino/arduino_keyboard_serial.html)  
>>[arduino中文社區](https://www.arduino.cn/thread-1066-1-1.html)  
>>[arduino葉難](http://yehnan.blogspot.com/2012/02/arduino_21.html)  
>>[arduino大兵萊恩](https://gogoprivateryan.blogspot.com/search/label/arduino)  
>>其中大兵萊恩裡面有很多有趣的作品       

教程用法:  
>>看懂本教程的內容    
>>完成網上教程的內容   
>>不要鑽研一些永遠都用不到的模塊  
>>遇到問題或其他改善建議可在下面留言  

## 正文
  
arduino是一部微處理器, 它能進行一些小的運算量  
同時它可以控制它針腳上的供電(output)以及測量針腳上的電壓(input)  
它可以和其他模塊進行通訊傳輸(SPI,I2C), 藍牙, wifi等  
一般初學時使用arduino uno, 功能是最差的, 但網上教程齊全  
熟悉uno後可以嘗試一下nano及mega2560  

下面比較一下各種板子

| 板子 | 特性 | 評價 | 價錢 | 推荐 |     
| - | :-: | :-: | -: |  
| Arduino uno | 容易上手, 資料齊全 | 功能很少, 體積不小 | RMB15 | *** |      
| Arduino nano | 容易上手, 和uno基本相同 | 功能最少, 體積很小 | RMB12 | ** |    
| Mega2560 | 不易上手, 資料較少 | 針腳很多, 體積很大 | RMB50 | * |     
| D1 mini | 超適合物聯網 | 具有wifi, 體積很小 | RMB12 | ***** | 
| NodeMCU ESP32 | 超適合物聯網 | 具有wifi, 體積很小 | RMB40 | ***** |  
| Raspberry Pi | 小型電腦, 可計算AI及調用cam | 可和Arduino結合 | RMB250 | 無法比較 |  
  
<img src="/img/arduino.png" width="40%">  Arduino uno  
<img src="/img/nano.jpg" width="40%">  Arduino nano   
<img src="/img/mega2560.jpg" width="40%">  Mega2560  
<img src="/img/d1_mini.jpg" width="40%">  d1 mini  
<img src="/img/nodemcu.jpg" width="40%">  NodeMCU ESP32  
<img src="/img/raspberry_pi.jpg" width="40%">  Raspberry Pi  
  
  
初學者的學習流程是:  
(1) 認識板子的腳位, 如何供電, 怎樣才能避免損壞板子    
(2) 使用UNO板練習接線, 點亮LED  
(3) 學習如何測量電壓, 光敏電阻的使用   
(4) 了解多一些Serial語法  
(5) 練習if, while, switch等邏輯語法  
(6) 練習下面表格中畫上紅線的傳感器  
(7) 練習藍牙, I2C傳輸  
(8) 使用d1 mini或NodeMCU練習wifi傳輸, 物聯網   
  

<p id = "build"></p>
---
  
  

## 練習



  
## 解答  
  
