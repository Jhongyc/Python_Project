# Author:GaoYuCai
name={"name":"Gao","age":23}
try:
    name['x']
    name[3]
except KeyError as e:
    print("键值出现错误",e)
except IndexError as e:
    print("索引值出现错误",e)
finally:
    print("检错完成！")