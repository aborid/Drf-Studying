from django.http import JsonResponse
from django.shortcuts import render
from rest_framework.generics import GenericAPIView
from rest_framework.views import APIView

from apps.user.models import User
from apps.user.serializers import UserSerializers
from utils import ResponseMessage
from utils.jwt_auth import create_token
from utils.password_encode import get_md5


# Create your views here.
class UserAPIView(APIView):

    # 注册功能的实现
    # def post(self, request):
    #     request.data["password"]=get_md5(request.data.get("password"))
    #     #反序列化 ，把json变成一个对象,这是关键的一句话
    #     user_data_serialzer=UserSerializers(data=request.data)
    #     user_data_serialzer.is_valid(raise_exception=True)
    #     user_data=User.objects.create(**user_data_serialzer.data)
    #     # 序列化，把json返回给前端
    #     user_ser=UserSerializers(instance=user_data)
    #     return JsonResponse(user_ser.data)

    def post(self, request):
        request.data["password"] = get_md5(request.data.get("password"))
        # 反序列化 ，把json变成一个对象,这是关键的一句话
        user_data_serialzer = UserSerializers(data=request.data)
        user_data_serialzer.is_valid(raise_exception=True)
        user_data = user_data_serialzer.save()
        # 序列化，把json返回给前端
        user_ser = UserSerializers(instance=user_data)
        # return JsonResponse(user_ser.data)
        return ResponseMessage.UserResponse.success(user_ser.data)
    def get(self,request):
        email = request.GET.get("email")
        try:
            user_data=User.objects.get(email=email)
            user_ser=UserSerializers(user_data)
            return ResponseMessage.UserResponse.success(user_ser.data)
        except Exception as e:
            print(e)
            return ResponseMessage.UserResponse.failed("用户信息获取失败")

class LoginView(GenericAPIView):
    def post(self, request):
        return_data={}
        request_data=request.data
        email=request_data.get("username")
        try:
            user_data=User.objects.get(email=email)
        except Exception:
            return ResponseMessage.UserResponse.other("用户名或者密码错误")
        if not user_data:
            return ResponseMessage.UserResponse.other("用户名或者密码错误")
        else:
            user_ser=UserSerializers(instance=user_data,many=False)
            # 用户输入的额密码
            user_password=request_data.get("password")
            md5_user_password=get_md5(user_password)
            #数据库密码
            db_user_password=user_ser.data.get("password")
            print(user_ser.data)
            if md5_user_password != db_user_password:
                return ResponseMessage.UserResponse.other("用户名或者密码错误")
            else:
                token_info={
                    "username":email
                }
                token_data=create_token(token_info)
                return_data["token"] = token_data
                return_data["username"] = user_ser.data.get("name")
                return ResponseMessage.UserResponse.success(return_data)






