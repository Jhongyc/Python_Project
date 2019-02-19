from django.shortcuts import render
from django.shortcuts import redirect
import os
# Create your views here.
from django.shortcuts import HttpResponse
# def index(request):
#     return HttpResponse("<h1>Hello  World!</h1>")
def login(request):
    # models.UserGroup.objects.create(caption='DBA')
    if request.method=="GET":
        return render(request,'login.html')
    elif request.method=="POST":
    #数据库中执行select * from user where username=‘’and pwd=’‘
        u=request.POST.get('user')
        p=request.POST.get('pwd')
        obj=models.UserInfo.objects.filter(username=u,pwd=p).first()
        if obj:
            return redirect('/app01/index/')
        else:
            return render(request,'login.html')
    else:
        return redirect('/index/')
from app01 import models
def orm(request):
    #增加数据
    # models.UserInfo.objects.create(
    #     username='root',
    #     pwd='123',
    # )
    # obj=models.UserInfo.objects.create(
    #     username='eric',
    #     pwd='123'
    # )
    # obj.save()
    # dic={'username':'eric','pwd':'123'}
    # models.UserInfo.objects.create(**dic)
    #查
    # result=models.UserInfo.objects.all()
    # result=models.UserInfo.objects.filter(username='eric')
    # for row in result:
    #     print(row.id,row.username,row.pwd)
    # print(result)
    #删除
    # models.UserInfo.objects.filter(id=3).delete()
    #更新
    # models.UserInfo.objects.all().update(pwd='333')
    return HttpResponse('orm')





from django.views import View
class Home(View):
    def dispatch(self, request, *args, **kwargs):
        result=super(Home,self).dispatch(request,*args,**kwargs)
        return result
    def get(self,request):
        return render(request,'home.html')
    def post(self,request):
        return render(request, 'home.html')
USER_DICT={
    '1':{'name':'root1','email':'root@qq.com'},
    '2':{'name':'root2','email':'root@qq.com'},
    '3':{'name':'root3','email':'root@qq.com'},
    '4':{'name':'root4','email':'root@qq.com'},
    #'1':'root1',
    # '2':'root2',
    # '3':'root3',

}
USER_LIST=[
    {'name':'root'}
]
# def index(request):
#     return render(request,'index.html',{'user_dict':USER_DICT})
def index(request):
    return render(request,'index.html')

def detail(request,nid):
    # nid=request.GET.get('nid')
    detail_info=USER_DICT[nid]
    return render(request,'detail.html',{'detail_info':detail_info})


