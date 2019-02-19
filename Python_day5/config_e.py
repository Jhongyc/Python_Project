# Author:GaoYuCai
import configparser
config=configparser.ConfigParser()
a=config.sections()
print(a)
print(config.read("example.ini"))
b=config.sections()
print(b)
for key in config['bitbucket.org']:
    print(key)