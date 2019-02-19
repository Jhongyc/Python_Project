# Author:GaoYuCai
import  configparser
conf=configparser.ConfigParser()
conf.read("example.ini")
print(conf.sections())
print(conf["DEFAULT"]["serveraliveinterval"])