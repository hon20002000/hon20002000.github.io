---
layout:     post
title:      "Quick_Start_Arduino_Lessons_4"
subtitle:   " \"IoT\""
date:       2019-08-04 16:00:00
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
>>[Cooper Maa](http://coopermaa2nd.blogspot.com/2011/02/arduino-serial-library.html)  
>>[arduino大兵萊恩](https://gogoprivateryan.blogspot.com/search/label/arduino)  
>>其中大兵萊恩裡面有很多有趣的作品       

## 正文
  
學習計劃:     
建議以葉難所寫的Arduino教學文為主, W3Cschool把所有知識點分得太細, 可作補充查詢    
  
下面根據葉難的教學文中挑選部分學習, 其餘文章並不需要  
[1. Arduino練習：PIR傳感器。](https://www.w3cschool.cn/arduino/arduino_pir_sensor.html)  
<img src="/img/PIR.jpg" width="40%">PIR傳感器  
PIR就是平常使用在感應人體紅外線的模塊, 當有人經過時就會檢測到。  
  
[2.1. Arduino練習：DHT11溫濕度傳感器。](https://a091234765.pixnet.net/blog/post/400005313-%5B%E7%AD%86%E8%A8%98%5Darduino%E5%AF%A6%E9%A9%97%E5%8D%81%E4%B8%80%3Adht11%E6%95%B8%E5%AD%97%E6%BA%AB%E6%BF%95%E5%BA%A6%E5%82%B3%E6%84%9F%E5%99%A8)  
[2.2. Arduino練習：DHT22溫濕度傳感器。](https://www.w3cschool.cn/arduino/arduino_humidity_sensor.html)
<img src="/img/DHT11.jpg" width="40%">DHT11溫濕度模塊  
<img src="/img/DHT22.jpg" width="40%">DHT22溫濕度模塊  
DHT11是便宜的藍色傳感器, DHT22是貴一點的白色傳感器, 學習了DHT11後再來學習DHT22。    

[3. Arduino練習：超聲波傳感器。](https://www.w3cschool.cn/arduino/arduino_ultrasonic_sensor.html)  
<img src="/img/HC_SR04.jpg" width="40%">HC-SR04超聲波模塊  
超聲波傳感器可以測量距離, 也可以觀察物件的移動。    
  
[4. Arduino練習：Serial語法。](http://coopermaa2nd.blogspot.com/2011/02/arduino-serial-library.html)  
當學習了一些模塊後, 初學者對Arduino已經有一定的了解, 慢慢開始希望輸出更多的data, 甚至和PC端或者其他設備互動。  
此時了解一下Serial的語法會很有幫助的。    

<p id = "build"></p>
---
