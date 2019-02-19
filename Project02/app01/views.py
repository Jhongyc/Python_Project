from django.shortcuts import render,HttpResponse,redirect
from app01 import  models
# Create your views here.
def business(request):
    v1=models.Business.objects.all().values('id','caption',)#拿到的是字典
    #QuerySet
    #[obj(id,cption,cod),obj(....),obj,obj]对象
    v2=models.Business.objects.all()
    v3=models.Business.objects.all().values_list('id','caption')#内部元素是元组
    return render(request,'business.html',{'v1':v1,'v2':v2,'v3':v3})

# def host(request):
#     v1=models.Host.objects.filter(nid__gt=0)
#      for row in v1:
#          print(row.nid,row.hostname,row.ip,row.port,row.b_id,row.b.caption,row.b.code,row.b.id,sep='\t')
#      return HttpResponse("Hello World!")
#     return render(request,'host.html',{'v1':v1})

def host(request):
    if request.method=='GET':
        v1=models.Host.objects.filter(nid__gt=0)
        # v2=models.Host.objects.filter(nid__gt=0).values("nid",'hostname','b_id','b_caption')
        # v3=models.Host.objects,filter(nid__gt=0).values_lsit("nid",'hostname','b_id','b_caption')
        b_list=models.Business.objects.all()
        return render(request, 'host.html', {'v1': v1,'b_list':b_list})
    elif request.method=="POST":
        h=request.POST.get('hostname')
        i=request.POST.get('ip')
        p=request.POST.get('port')
        b=request.POST.get('b_id')
        models.Host.objects.create(hostname=h,ip=i,port=p,b_id=b)
        return  redirect('/host')
def test_ajax(request):
    # print(request.method,request.GET.get("username"),request.GET.get('pwd'),sep='\t')
    # return  HttpResponse('Hello World!')
    h=request.POST.get('hostname')
    i=request.POST.get('ip')
    p=request.POST.get('port')
    b=request.POST.get('b_id')
    if h and len(h) > 5:
        models.Host.objects.crate(
            hostname=h,
            ip=i,
            port=p,
            b_id=b
        )
        return  HttpResponse("OK")
    else:
        return HttpResponse('太短了')


