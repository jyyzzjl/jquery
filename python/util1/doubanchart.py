'''
Created on 2015年10月24日

@author: lenovo
'''
import mongdb
import requests
import re
import json

#最新电影的首页
url="http://movie.douban.com/chart"
#最新电影的正则表达式，要获取名称，简介，评分，评价人数
pattern = re.compile('<tr.*?item.*?title="(.*?)".*?"pl">(.*?)</p>.*?rating_nums">(.*?)</span>.*?pl">\((.*?)人评价\)</span>',re.S)

#定义获取的movie
class Movie():
    def __init__(self,name,summary,scroe,num):
        self.name=name
        self.summary=summary
        self.scroe=scroe
        self.num=num
'''豆瓣抓包方法
aaaa'''
class doubanchart():
    def __init__(self,url):
        self.url=url
        pass
    #根据url获取所有的最新电影的列表
    def getContent(self):
        r=requests.get(self.url);
        
        #根据主页获取所有的糗事
        allItems=re.findall(pattern,r.text)
        return allItems
    #保存最新电影信息到mongdb
    def saveContent(self,items):
        mongdb.insert('douban', items)
        
    def getItems(self,items={}):
        return mongdb.getItem("douban", items)

#初始化豆瓣类
douban=doubanchart(url)
content=douban.getContent()
movies=[]

#将内容插入mongdb
for x in content:
    movie=Movie(x[0],x[1],x[2],x[3])
    #print(json.dumps(movie, default=convert_to_builtin_type))
    #douban.saveContent(convert_to_builtin_type(movie))
    douban.saveContent((lambda movie:{'name':movie.name,'summary':movie.summary,'scroe':movie.scroe,'num':movie.num})(movie))
 
 #从mongdb中获取内容，并显示
 
for item in douban.getItems():
     print("书名：{}\n评分{}\n人数{}".format(item['name'],item['scroe'],item['num']))

#print(movies)





