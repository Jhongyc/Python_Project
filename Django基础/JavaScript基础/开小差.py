# Author:GaoYuCai
import  requests
i1=requests.get(url="http://dig.chouti.com/help/service")
i2=requests.post(url="http://dig.chouti.com/login",data={
    "phone":"","password":"密码","oneMonth":""
},cookies=i1.cookies.get_dict())