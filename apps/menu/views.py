import json

from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from .models import MainMenu, SubMenu
from utils import ResponseMessage

# Create your views here.
class GoodsMainMenu(View):
    def get(self,request):
        print("get请求来了")
        main_menu=MainMenu.objects.all()
        result_list=[]
        for m in main_menu:
           # result_list.append(m)
            result_list.append(m.__str__())
        # result_json["status"]=1000
        # result_json["data"]=result_list
        # return HttpResponse(json.dumps(result_json),content_type="application/json")
        return ResponseMessage.MenuResponse.success(result_list)

    def post(self,request):
        print("post请求来了")
        return HttpResponse("post请求")
class GoodsSubMenu(View):
    def get(self,request):
        #获取请求的参数
        param_id=request.GET["main_menu_id"]
        print(param_id)
        #拿到二级菜单的内容
        sub_menu = SubMenu.objects.filter(main_menu_id=param_id)
        result_list = []
        result_json = {}
        for m in sub_menu:
            # result_list.append(m)
            result_list.append(m.__str__())
        # result_json["status"] = 1000
        # result_json["data"] = result_list
        return ResponseMessage.MenuResponse.success(result_list)
        # return HttpResponse(json.dumps(result_json), content_type="application/json")
