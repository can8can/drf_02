from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.utils.decorators import method_decorator

# Create your views here.
from django.views import View
from django.views.decorators.csrf import csrf_exempt, csrf_protect

from rest_framework.views import APIView
from rest_framework.response import Response

# @csrf_protect
from app1.models import User


@csrf_exempt  #为视图免除csrf认证
def user(request):
    if request.method == 'GET':
        print("GET 查询成功")
        print(request.GET.get("username"))
        return HttpResponse("GET 查询成功")

    if request.method == 'POST':
        print("POST 增加成功")
        print(request.POST.get("username"))
        return HttpResponse("POST 增加成功")

    if request.method == 'PUT':
        print("GET 修改成功")
        return HttpResponse("GET 修改成功")

    if request.method == 'DELETE':
        print("POST 删除成功")
        return HttpResponse("POST 删除成功")



#类视图
@method_decorator(csrf_exempt, name='dispatch')
class UserView(View):
    def get(self,request,*args,**kwargs):
        print("GET 请求  查询")
        return HttpResponse("GET 请求成功")

    def post(self,request,*args,**kwargs):
        print("POST 请求  新增")
        return HttpResponse("POST 请求成功")

    def put(self,request,*args,**kwargs):
        print("PUT 请求  更新")
        return HttpResponse("PUT 请求成功")

    def delete(self,request,*args,**kwargs):
        print("DELETE 请求  删除")
        return HttpResponse("DELETE 请求成功")


@method_decorator(csrf_exempt,name="dispatch")
class EmployeeView(View):
    def get(self,request,*args,**kwargs):
        user_id=kwargs.get("id")
        if user_id:
            #user_obj=User.objects.get(pk=user_id)
            user_obj = User.objects.filter(pk=user_id).values("username","password","gender","email").first()
            print(user_obj,type(user_obj))
            if user_obj:
                return JsonResponse({
                    "status":200,
                    "message":"查询单个用户成功",
                    "results":user_obj
                })
        else:
            user_list=User.objects.all().values("username","password","gender","email")
            print(user_list,type(user_list))
            return JsonResponse({
                "status": 200,
                "message": "查询所有用户成功",
                "results": list(user_list)
            })
        return JsonResponse({
            "status": 500,
            "message": "不存在",
        })


    def post(self,request,*args,**kwargs):
        username=request.POST.get("username")
        pwd = request.POST.get("pwd")
        gender = request.POST.get("gender")
        email = request.POST.get("email")
        print(username,pwd,gender,email)

        try:
            user_obj=User.objects.create(username=username,password=pwd,gender=gender,email=email)
            return JsonResponse({
                "status": 200,
                "message": "创建用户成功",
                "results": {"username": user_obj.username, "password":user_obj.password,"gender":user_obj.gender,"email": user_obj.email,}

            })
        except:
            return JsonResponse({
                "status": 500,
                "message": "创建用户失败",})

@method_decorator(csrf_exempt,name="dispatch")
class UserAPIView(APIView):

    def get(self, request, *args, **kwargs):
        print("这是drf的get请求")
        return Response("DRF GET OK")

    def post(self, request, *args, **kwargs):
        print("这是drf的post请求")
        return Response("DRF POST OK")
