from django.shortcuts import render
from rest_framework.views import APIView
from django.http import HttpResponse, JsonResponse

from apps.cart.models import Cart
from apps.cart.serializers import CartDetailSerializer, CartSerializer
from utils import ResponseMessage


# Create your views here.
class CartAPIView(APIView):
    #购物车应该是登录后才能访问的
    # @todo 后续补充登录权限认证

    def post(self,request):
        request_data = request.data
        # print(request_data)
        # print(type(request_data))
        # email=request_data.get('email')
        if not request.user.get("status"):
            return JsonResponse(request.user, safe=False)
        email=request.user.get("data").get("username")
        request_data["email"] = email
        sku_id=request_data.get("sku_id")
        nums=request_data.get("nums")
        is_delete=request_data.get("is_delete")

        #判断一下数据是否存在，如果存在就更新，如果不存在就插入
        print(request_data)
        data_exist=Cart.objects.filter(email=email,
                            is_delete=is_delete,
                            sku_id=sku_id)
        if data_exist.exists():
            exists_cart_data=data_exist.get(
                email=email,
                is_delete=0,
                sku_id=sku_id
            )
            new_nums=nums+exists_cart_data.nums
            request_data["nums"]=new_nums
            #反序列化
            cart_ser =CartSerializer(data=request_data)
            #更新
            cart_ser.is_valid(raise_exception=True)
            Cart.objects.filter(email=email,is_delete=0,sku_id=sku_id).update(**cart_ser.data)
            # return HttpResponse("更新成功")
            return ResponseMessage.CartResponse.success("更新成功")
        else:
            #这里是数据插入逻辑
            cart_ser=CartSerializer(data=request_data)
            cart_ser.is_valid(raise_exception=True)
            Cart.objects.create(**cart_ser.data)

            # return HttpResponse("数据插入成功")

            return ResponseMessage.CartResponse.success("插入成功")
    def get(self,request):
        if not request.user.get("status"):
            return JsonResponse(request.user,safe=False)
        email=request.GET.get('email')
        cart_result=Cart.objects.filter(email=email,is_delete=0)
        cart_ser=CartSerializer(instance=cart_result,many=True)
        return ResponseMessage.CartResponse.success(cart_ser.data)
# 使用序列化器进行序列化查询
class CartDetailView(APIView):
    def post(self,request):
        if not request.user.get("status"):
            return JsonResponse(request.user,safe=False)
        email=request.user.get("data").get("username")
        filters={
            "email":email,
            "is_delete":0,
        }
        shopping_cart =Cart.objects.filter(**filters).all()
        db_data=CartDetailSerializer(shopping_cart,many=True)
        return ResponseMessage.CartResponse.success(db_data.data)
class UpdateCartNumAPIView(APIView):
    def post(self,request):
#         从token中获取email
        if not request.user.get("status"):
            return JsonResponse(request.user, safe=False)
        email=request.user.get("data").get("username")
        request_data=request.data
        Cart.objects.filter(
            email=email,
            sku_id=request_data["sku_id"],
            is_delete=0
        ).update(nums=request_data["nums"])
        return ResponseMessage.CartResponse.success("ok")

# 获取购物车商品数量的接口
class CartCountAPIView(APIView):
    def post(self,request):
        if not request.user.get("status"):
            return JsonResponse(request.user, safe=False)
        email=request.user.get("data").get("username")
        from django.db.models import Sum
        user_cart_count=Cart.objects.filter(
            email=email,
            is_delete=0
        ).aggregate(Sum("nums"))
        return ResponseMessage.CartResponse.success(user_cart_count)
class DeleteCartGoodsAPIView(APIView):
    def post(self,request):
#         从token中获取email
        if not request.user.get("status"):
            return JsonResponse(request.user, safe=False)
        email=request.user.get("data").get("username")
        request_data=request.data
        Cart.objects.filter(
            email=email,
            sku_id__in=request_data,
            is_delete=0
        ).update(is_delete=1)
        return ResponseMessage.CartResponse.success("ok")
