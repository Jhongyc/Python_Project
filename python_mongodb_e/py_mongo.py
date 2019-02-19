# Author:GaoYuCai
import pymongo
connection=pymongo.MongoClient("192.168.80.11",27017)
tdb=connection.alpha87
post=tdb.test
post.insert({'name':"李白",'age':'30','skill':'Python'})
print('操作完成')