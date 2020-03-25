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

## 把label貼在view上 
  
我們在Xcode介面的右上角可以找到'＋'按鈕  
找出label拉到view上  
<img src="/img/label.gif" width="70%">  
按右上角的分屏按鈕，開出一個版面，選擇左邊的viewController.swift  
那麼畫面便會進入coding部分，將label(按住control然後用左鍵)拉到code中的class ViewController: UIViewController裡面  
這時需要幫label命名(例如label1)，coding中便可以使用此命名來控制此label  
那麼view和controller的連結便完成  
<img src="/img/label_link.gif" width="70%">  
成功連結的code旁邊會有一個黑色圓點(若是空心圓點表示沒有連結)  
<img src="/img/linking.png" width="70%">  
這時按play運行模擬器便可以成功  
<img src="/img/show.png" width="25%">  

## 把imageView貼在view上
  
 imageView是盛載圖片的載體(相框)，圖片會被限制在特定的大小下顯示  
 同樣地我們在右上角的'+'拉出imageView到view上  
 並連結imageview和viewcontroller  
 要顯示圖片要先把圖片拉到Assets.xcassets上(main.storyboard下面的文件夾)  
<img src="/img/a1.gif" width="70%">  
<img src="/img/imageView.gif" width="70%">  
然後我們把畫面轉到viewController.swift中  
在super.viewDidLoad()下面加入  
imageView.image = UIImage(named: "a1.jpg")  
此句code的意思是 imageView相框.圖片 = "a1.jpg"
<img src="/img/imageView2.png" width="80%">  
   
## 使用button控制label和imageView上的顯示  
  
我們拉出button，貼在view上並連結去viewController.swift上  
button連結時有outlet和action兩個選擇，outlet表示只作顯示  
action則表示按下button時執行其他功能  
選擇action後並命名button  
並在button的action內加入function -- showPicture()  
然後我們在code的最下方加上function的內容  
  
    func showPicture(){
        imageView.image = UIImage(named:"a1.jpg")
        label1.text = "以津真天"
    }  
    
<img src="/img/button.gif" width="70%">     
三項功能的完整code如下
  
    import UIKit

    class ViewController: UIViewController {
        @IBAction func button(_ sender: Any) {
            showPicture()
        }
        
        @IBOutlet weak var label1: UILabel!
        
        @IBOutlet weak var imageView: UIImageView!
        override func viewDidLoad() {
            super.viewDidLoad()
        }
        func showPicture(){
            imageView.image = UIImage(named: "a1.jpg")
            label1.text = "以津真天"
        }
    }    
<img src="/img/press_button.gif" width="70%">    
接下來若想回復原狀，則可新設多一個button  
用同樣的方法操作，並設置新的function為cancel  
  
    func showPicture(){
      imageView.image = nil
      label1.text = "SHOW"
    }  
  
可以自行嘗試    
<img src="/img/press_button2.gif" width="25%">    
