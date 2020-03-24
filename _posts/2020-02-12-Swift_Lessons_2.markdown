---
layout:     post
title:      "Swift_Lessons_2"
subtitle:   " \"使用TableView顯示遠端資料 - Google Spreadsheet JSON & Imgur  (2)\""
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
  
本教程參考自(https://ccng830.github.io/2020/03/03/Google-Spreadsheet-JSON-&-imgur(2)/)   
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
我們在此專案下使用pod生成新的插件專案  
找出此API_test文件的路徑，開啟終端機後前往此文件夾  
(1)cd file_path  
(2)pod init  
<img src="/img/pod_init.png" width="70%">    

文件夾下會新增了podfile，打開podfile後  
<img src="/img/podinit.png" width="70%">    
加上pod 'SDWebImage', :modular_headers => true  
<img src="/img/SDWebImage.png" width="70%">  
然後再在終端機輸入pod install  
成功後API_test的文件夾下會生成一個新的專案  
若顯示錯誤則可能是大小寫問題或少了一些標點符號
<img src="/img/pod_workspace.png" width="70%">   
我們使用此專案來開發app  

接下來我們在API_Test下的Info.plist開放手機的權限   
點一下Information Property List，然後按'+'，加入App Transport Security Settings    
然後同樣在App Transport Security Settings上點一樣，然後按'＋'  
加入Allow Arbitrary Loads，並選擇yes  
<img src="/img/2.gif" width="70%">   
  
接下來在storyboard的view controller上加入Navigation controller  
並在view controller的Navigation bar上的title改為pokemon(可以改其他名稱)  
<img src="/img/3.gif" width="70%">   

拉入table view  按著control及滑鼠左鍵連上dataSource及delegate,   
以及table view要連上viewcontroller.swift  
<img src="/img/4.gif" width="70%">   
  
viewcontroller.swift上要手動加上UITableViewDataSource, UITableViewDelegate  
等一會後系統警告需要fix error，按fix便可  
<img src="/img/tableview.png" width="70%">    
  
總結如下：    
(1)tableview 連上UITableViewDataSource, UITableViewDelegate  
(2)tableview 連上viewcontroller.swift的outlet  
(3)viewcontroller.swift上手動加上UITableViewDataSource, UITableViewDelegate 並fix  

最後只要copy下面的code copy到viewcontroller.swift上便完成  
    
    
    import UIKit
    import SDWebImage

    class ViewController: UIViewController, UITableViewDelegate, UITableViewDataSource  {
        
        var pokeDetail: [String] = []
        var url = [String]()
        @IBOutlet weak var myTableView: UITableView!
        
        func tableView(_ tableView: UITableView, numberOfRowsInSection section: Int) -> Int {
            return pokeDetail.count
        }
        
        func tableView(_ tableView: UITableView, cellForRowAt indexPath: IndexPath) -> UITableViewCell {
            tableView.rowHeight = 180
            let cell = UITableViewCell(style: UITableViewCell.CellStyle.default, reuseIdentifier: "Cell")
            cell.imageView?.sd_setImage(with: URL(string: url[indexPath.row]))
            cell.textLabel?.text = pokeDetail[indexPath.row]
            return cell
        }
        
        override func viewDidLoad() {
            super.viewDidLoad()
            getpokeData()
        }

        //MARK: --- Pokemon API
        struct PokeResults: Codable {
            let rows: [Poke]
        }

        struct Poke: Codable {
            let num: String
            let name: String
            let property: String
            let image: String
        }

        func getpokeData() {
            let address = "http://gsx2json.com/api?id=1RvCfk-bgIt4UHOzwIYtt0P3VFv8Iutj7wUKdKQQS-_8&columns=false"
            if let url = URL(string: address) {
                // GET
                URLSession.shared.dataTask(with: url) { (data, response, error) in
                    if let error = error {
                        print("Error: \(error.localizedDescription)")
                    } else if let response = response as? HTTPURLResponse,let data = data {
                        print("Status code: \(response.statusCode)")
                        let decoder = JSONDecoder()
                        
                        if let pokeResults = try? decoder.decode(PokeResults.self, from: data) {
                            DispatchQueue.main.async{
                                for poke in pokeResults.rows {
                                    self.pokeDetail.append(poke.num + " " + poke.name + " " + poke.property)
                                    self.url.append(poke.image)
                                }
                                self.myTableView.reloadData()
                            }
                        }
                    }
                }.resume()
            } else {
                print("Invalid URL.")
            }
        }
        
    }



