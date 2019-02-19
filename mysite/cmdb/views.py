
# Create your views here.
from django.shortcuts import HttpResponse
# from django.shortcuts import render
# def login(requset):
    # f=open("templates/login.html",'r',encoding="utf-8")
    # data=f.read()
    # f.close()
    # return HttpResponse(data)
#     return render(requset,"login.html")
#
from django.shortcuts import render
from  django.shortcuts import redirect
def home(request):
     return HttpResponse("<h1>CMDB</h1>")

def login(request):
     error_msg=''
     if request.method == "POST":
          user = request.POST.get('user',None)
          pwd  = request.POST.get('pwd',None)
          if user == "root" and pwd =="123":
               return redirect('/home')
          else:
               error_msg='用户名或者密码错误。'

     return render(request,'login.html',{'error_msg':error_msg})
USER_LIST=[
     {'username':'alex','email':'...@qq.com','gender':"男"},
]
# for item in range(20):
#      temp={'username':'alex'+str(item),'email':'...@qq.com','gender':"男"}
#      USER_LIST.append(temp)
def home(request):
     if request.method=='POST':
          u=request.POST.get('username')
          e=request.POST.get('email')
          g=request.POST.get('gender')
          temp = {'username': u, 'email': e, 'gender': g}
          USER_LIST.append(temp)
     return render(request,'home.html',{'user_list':USER_LIST})