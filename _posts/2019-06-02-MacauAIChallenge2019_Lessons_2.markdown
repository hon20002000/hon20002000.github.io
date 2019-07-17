---
layout:     post
title:      "MacauAIChallenge2019_Lessons_2"
subtitle:   " \"Digital classification\""
date:       2019-06-02 16:00:00
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

在使用CNN進行我們的比賽之前，我們先學習分辨最基礎的0~9數字圖像  
0~9數字圖像的數據訓練集名稱叫作mnist，它是可以直接在spyder下載的  
mnist是一個含有60000張28x28像素的training data  
及10000張28x28像素的testing data的手寫數字圖片  
我們的目標就是利用神經網絡neural network來分辨數字  
  
>概念流程:  
>(1)load_data    #下載數據集  
>(2)reshape data    #把28*28數據變成784*1, 因為neural network需要這種shape的數據形式來學習
>(3)把label由0~9變為二進制的one-hot編碼, 例如  
>(0)=[1,0,0,0,0,0,0,0,0,0], (1)=[0,1,0,0,0,0,0,0,0,0]     
>(4)建立模型 model.Sequential() > models.Dense > layers.Activation > model.summary > model.compile > model.fit

下面是完整程式碼:    
  
    #使用keras作為我們的語法並import有用的function  
    import keras    
    from keras.datasets import mnist    
    from keras.models import Sequential    
    from keras.layers import Dense, Dropout, LeakyReLU, Conv2D
    from keras.optimizers import RMSprop    #optimizer可選擇rmsprop, adadelta, adam, sgd
    from keras import backend as K
    from matplotlib.pyplot import imshow   #顯示圖片的function
    import numpy as np    #運算工具
    
    # loading train and test sets and reshape
    (x_train, y_train), (x_test, y_test) = mnist.load_data()   #讀取data
    x_train = x_train.reshape(60000, 784)    #x=data, y=label, reshape (28x28) -> (784,)
    x_test = x_test.reshape(10000, 784)    #60000 training data, 10000 test data
    x_train = x_train.astype('float32')    #由於像數值為0~255的整數, 把它轉為float作計算
    x_test = x_test.astype('float32')
    x_train /= 255    #把0~255/255即是把數字轉為0~1, 意義是運算的數值變小
    x_test /= 255

    num_classes = 10
    # convert class vectors to binary class matrices
    y_train = keras.utils.to_categorical(y_train, num_classes)    #把數字由0~9轉為one-hot編碼
    y_test = keras.utils.to_categorical(y_test, num_classes)


    model = models.Sequential()
    model.add(layers.Dense(1024, input_shape=(784,)))    #first layer need to input data shape
    model.add(layers.Activation("relu"))    #neural network一般使用relu
    model.add(layers.Dense(128))     #dense(128) include 128 parameters in a layer
    model.add(layers.Activation("relu"))
    model.add(layers.Dense(10))    #最後一層等於分類數目
    model.add(layers.Activation("softmax"))    #最後一層使用softmax 
    model.summary()

    model.compile(loss='categorical_crossentropy',   #多分類使用categorical_crossentropy
                  optimizer='rmsprop',    #optimizer一般有adam, adadelta, rmsprop, sgd等等  
                  metrics=['accuracy'])    

    batch_size = 128    #batch_size越大每次訓練的數據越多, 注意記憶體可能會不夠用  
    num_classes = 10    
    epochs = 10    #重覆訓練10輪
    history = model.fit(x_train, y_train,    #model.fit才是正式訓練模型, 上面只是設定model
                        batch_size=batch_size,
                        epochs=epochs,
                        verbose=1,      #verbose=1表示顯示進度條, 共有0,1,2三種模式
                        validation_data=(x_test, y_test))   
    
下面詳細講解這段程式碼    
首先要有的概念就是，我們手上將要處理的數據的shape是怎樣的?  
我們使用的model能接受的shape又是什麼?  
只要這兩個shape是符合的, 那就能訓練model  
另外, label是數字或是one-hot是自行決定的, 一般慣例使用one-hot  
訓練模型的層數是隨意的, activation一般是relu  
最後一層是分類的數目, 使用softmax作分類  
softmax的特點是所有類別的result加起來等於1, 因此有機率的意味  
我們先看看mnist的一個data是怎樣的數據  
在(x_train, y_train), (x_test, y_test) = mnist.load_data()下面加上  

    (x_train, y_train), (x_test, y_test) = mnist.load_data()    #下載mnist數據集
    imshow(x_train[0], cmap='gray')
    print("x_train[0]:", x_train[0])
    print("x_train[0].shape:", x_train[0].shape)
    print("y_train:", y_train)
    print("y_train.shape:", y_train.shape)
    print("y_test:", y_test)
    print("y_test.shape:", y_test.shape)
  
可觀察到如下的結果:  
<img src="img/mnist_5.png" width="40%">  
<img src="img/dense.png" width="40%">  
<img src="img/mnist_result.png" width="40%">  
<img src="img/master.jpg" width="40%">  
<img src="img/cc.jpg" width="40%">  

## 練習
  
(1)什麼是監督式學習(Supervised learning)?  
(2)什麼是神經網絡(neural network)?  
(3)什麼是深度學習(deep learning)?  
(4)mnist數據集是什麼, 用什麼方法完成分類? 
(5)carfi10數據集是什麼, 用什麼方法完成分類? 

---


