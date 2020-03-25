---
layout:     post
title:      "Swift_Lessons_5"
subtitle:   " \"使用TableView顯示遠端資料 - Google Spreadsheet JSON & Imgur (1)\""
date:       2020-02-11 16:00:00
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

開發iOS App時，我們都希望App內顯示的資料 (文字、數據、圖片等等)來自網絡上，  
因此更新數據就來得更加容易。   
而本文所介紹的方法適合單純地從網路抓資料顯示，不需要修改或上傳資料。  
我們需要利用網上的免費空間來儲存或讀取資料，例如表格資料及圖片。   
本範例使用Google Spreadsheet & imgur來儲存資料，我們一需要把表格資料轉換成 JSON 然後和 iOS App 串接。  

## 申請imgur的account  
  
首先利用imgur來上載一些圖片，目的是獲得圖片的url  
注意圖片的url含有.jpg或.png等副檔名(https://i.imgur.com/rOFDO9i.jpg)  
而不是網站的url(https://hon20002000.imgur.com/all)  
在imgur注冊一個帳號，然後上傳圖片，最後點擊圖片把url copy到試算表上  
<img src="/img/1.gif" width="70%">  
  
## 建立Google Spreadsheet
  
搜尋Google Spreadsheet(Google 試算表)，即下面的link  
https://docs.google.com/spreadsheets/u/0/    
按右下角的按鈕，新增Spreadsheet  
  
<img src="/img/new_sheet.png" width="30%">    

輸入如下圖中的資料，copy圖片在 imgur的網址。   
注意儲存格中所有數據都必須是String格式，否則在Swift後面的處理會遇到麻煩。  
例如數字1在儲存格被定義為Int，而No.001則被定義為String，這是要注意的。  
<img src="/img/20200224.png" width="70%"> 
  
然後在google sheet的檔案按發佈到網路  
<img src="/img/20200224_1.png" width="50%">  
  
## 把google sheet的資料轉換成JSON的格式  
  
我們利用gsx2json把我們的google sheet轉換成swift可使用的json格式    
轉換方法是把下面網址上的xxxxx替換成你google sheet上的網址id  

http://gsx2json.com/api?id=xxxxxxx&columns=false  

google sheet網址上其中一段文字即為id  
<img src="/img/link.png" width="100%">  
  
若成功後輸入網址將會顯示你輸入的資料，這網址可以被swift使用，如下圖所示：
  
<img src="/img/gsx2json.png" width="100%">    
  
此網址上的資料沒有排版很混亂，我們可以把資料copy到Json Editor Online來顯示得更清楚  
(swift上不會用到son Editor Online，此網站只是讓我們了解JSON是如何排列資料)  
http://jsoneditoronline.org/#left=local.woxipo&right=local.nenoge  
將所有資料copy後，貼到左側，再按下「Copy > 」的按鈕  
如此右側便會顯示我們排版後的資料結構    
<img src="/img/jsoneditonline.png" width="80%">   
>下一教程將使用gsx2json上的資料來制作app  
 
