---
layout:     post
title:      "Quick_Start_Arduino_Lessons_2"
subtitle:   " \"Arduino_practices_1\""
date:       2019-08-02 16:00:00
author:     "hon20002000"
header-img: "img/Python.png"
catalog: true
tags:
    - Arduino Quick Start 
---
## 前言
  
'''  
作者: hon20002000   
最後更新: 2019/9/24    
'''   
  
本教程是為了讓同學們快速學習Arduino, 開發物聯網應用而設計的.  

>由於arduino的入門教程實在太多    
>因此這裡就不再重新寫作一份教程了     
>這裡簡單介紹一下arduino自學中的重點以及特別要注意的地方     
>>網上資源可以看  
>>[W3Cschool](https://www.w3cschool.cn/arduino/arduino_keyboard_serial.html)  
>>[arduino中文社區](https://www.arduino.cn/thread-1066-1-1.html)  
>>[arduino葉難](http://yehnan.blogspot.com/2012/02/arduino_21.html)  
>>[arduino大兵萊恩](https://gogoprivateryan.blogspot.com/search/label/arduino)  
>>[Cooper Maa](http://coopermaa2nd.blogspot.com/2011/02/arduino-serial-library.html)  
>>其中大兵萊恩裡面有很多有趣的作品       

## 正文
  
學習計劃:     
建議以葉難所寫的Arduino教學文為主, W3Cschool把所有知識點分得太細, 可作補充查詢    
  
下面根據葉難的教學文中挑選部分學習, 其餘文章並不需要  
[1. Arduino練習：以開關切換LED明滅狀態，以開關點亮、熄滅LED，並且解決bounce問題。](http://yehnan.blogspot.com/2012/02/arduinoled.html)  
本實驗的難點在於後面的Bounch問題, 剛開始學習的時候不明白可以跳過, 直到該問題困擾了你的實驗作品  
注意#define PIN 2和int PIN = 2的意思是相同的, 都是用來命名參數    
  
[2. Arduino練習：以開關切換LED是否閃爍，沒有太多說明，示範兩種技巧達成想要的功能，一種不使用delay只使用millis，一種使用現成的程式庫。](http://yehnan.blogspot.com/2014/03/arduinoled.html)  
delay函數會使整個程序停頓, 而millis則不會停頓, 算是計時的高級技巧, 若delay對你的實驗作品影響很大, 則換成millis來計時  

[3. Arduino練習：呼吸燈，以PWM讓LED漸亮漸暗，顯現呼吸效果，類似於蘋果電腦的電源指示燈；以可變電阻控制呼吸循環週期的時間長短。](http://yehnan.blogspot.com/2012/02/arduino_16.html)  
理解PWM原理  
  
[4. Arduino練習：光敏電阻， 以光敏電阻控制LED的明滅。](http://yehnan.blogspot.com/2012/02/arduino_23.html)  
<img src="/img/photoresistance.jpg" width="40%">RGB模塊  
光敏電阻的用途是利用電阻之間的比較, 測量它的電壓值, 通過語法來控制其他元件  
  
[5. Arduino練習：RGB LED，可發出各種顏色光芒的RGB LED。](http://yehnan.blogspot.com/2013/01/arduinorgb-led.html)  
<img src="/img/RGB_LED.jpg" width="40%">RGB模塊  
簡單的三色LED燈練習, 市面上有更美觀的模塊    
   
[6. Arduino練習：溫度感測DS18B20，使用OneWire與DallasTemperature程式庫，輕鬆讀取溫度感測器DS18B20。](http://yehnan.blogspot.com/2013/01/arduinods18b20.html)  
<img src="/img/DS18B20.png" width="40%">DS18B20溫度傳感器  
葉難所用的DS18B20並不是模塊, 如果是模塊的話就不用再加上電阻, 但原理是一樣的  
  
[7. Arduino練習：伺服馬達以Tower Pro SG90為例，簡介伺服馬達，以便宜的Tower Pro SG90為範例。](http://yehnan.blogspot.com/2013/09/arduinotower-pro-sg90.html)  
<img src="/img/SG90.jpg" width="40%">RGB模塊  
學習伺服馬達可以使自己的作品動起來  
  
<p id = "build"></p>
---
  
