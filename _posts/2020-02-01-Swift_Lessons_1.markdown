---
layout:     post
title:      "Swift_Lessons_1"
subtitle:   " \"使用UIImageView, UILabel, UIButton\""
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
  
## 正文

我們在開發IOS app時，需要使用label來顯示文字訊息  
用imageView來顯示圖片  
並且使用button來進行一些操作  

本範例簡單地說明在swift中如何使用這三個功能    
swift中在進行coding前要先了解一下下面的概念圖  

<img src="/img/swift_concept1.png" width="70%">    
<img src="/img/swift_concept2.png" width="70%">  
一個app的運行由3部分構成  
第一部分是view，即是用戶能看到的介面  
第二部分是controller，，即是控制和更新view介面的代碼部分  
第三部分是model，包含app需要使用的文件及資料  
我們暫時先了解view和controller的關係  
由於view被controller控制，所以view上的label，button等必須和controller連繫  
但是swift不會自動將你在view上的label等和controller上的code連接  
因此初學者最容易出現的bug就是忘記把view和controller連線  
下面開始本教程的操作  

## 搜索及貼上label在view上 
  
我們在Xcode介面的右上角可以找到'＋'按鈕  
找出label拉到view上  
<img src="/img/label.gif" width="70%">  
按右上角的分屏按鈕，開出一個版面，選擇左邊的viewController.swift  
那麼畫面便會進入coding部分，將label拉到code中的class ViewController: UIViewController裡面  
那麼view和controller的連結便完成  
<img src="/img/label_link.gif" width="70%">  
這時按play運行模擬器便可以成功  
<img src="/img/show.png" width="70%">  

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
 
