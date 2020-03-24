---
layout:     post
title:      "Swift_Lessons_2"
subtitle:   " \"利用Google Spreadsheet JSON & Imgur 開發App (2)\""
date:       2020-02-12 16:00:00
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

下面是本app的成品，通過table view來顯示網路上的資料。   
<img src="/img/API_test.gif" width="30%">    
  
## 使用SDWebImage插件獲取網路圖片  
SDWebImage是一款第三方插件用來處理app的圖片下載問題  
能夠即時下載並顯示在app中  
主流的app(微信和QQ)也會用此插件  
<img src="/img/sdwebimage.png" width="70%">    

我們首先在XCode中開啟新project，取名API_test後關閉它  
找出此API_test文件的路徑，開啟終端機後前往此文件夾  
即是cd file_path，enter後再輸入pod init  
<img src="/img/pod_init.png" width="70%">    


 
  
## 建立Google Spreadsheet
  

  
## 把google sheet的資料轉換成JSON的格式  
  
