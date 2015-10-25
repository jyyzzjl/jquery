from pymongo import MongoClient

'''获得数据库链接，并切换到指定的db'''
def getDB(dbName):
    conn=MongoClient()
    db=conn[dbName]
    return db

def getOne(dbName,se={}):
    db=getDB(dbName)
    return db[dbName].find_one(se)

def getItem(dbName,se={}):
    db=getDB(dbName)
    return db[dbName].find(se)


def insert(dbName,se={}):
    db=getDB(dbName)
    print(type(se))
    return db[dbName].insert(se)


#insert('douban', {'name':'zhangsan'})

getItem('douban')
    


