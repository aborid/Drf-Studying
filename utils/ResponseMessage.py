import json

from django.http import HttpResponse, JsonResponse


#菜单是第一开发的
# 成功了就是1000
# 失败了就是1001
# 其他不确定的是1002


class MenuResponse():

    @staticmethod
    def success(data):
        result={"status":1000,"data":data}
        return HttpResponse(json.dumps(result), content_type = "application/json")


    @staticmethod
    def failed(data):
        result = {"status": 1001, "data": data}
        return HttpResponse(json.dumps(result), content_type="application/json")

    @staticmethod
    def other(data):
        result = {"status": 1002, "data": data}
        return HttpResponse(json.dumps(result), content_type="application/json")
class GoodsResponse():

    @staticmethod
    def success(data):
        result={"status":2000,"data":data}

        return HttpResponse(json.dumps(result), content_type = "application/json")


    @staticmethod
    def failed(data):
        result = {"status": 2001, "data": data}
        return HttpResponse(json.dumps(result), content_type="application/json")

    @staticmethod
    def other(data):
        result = {"status": 2002, "data": data}
        return HttpResponse(json.dumps(result), content_type="application/json")

#购物车响应
class CartResponse():
    @staticmethod
    def success(data):
        result = {"status": 3000, "data": data}
        return JsonResponse(result,safe=False)

    @staticmethod
    def failed(data):
        result = {"status": 3001, "data": data}
        return JsonResponse(result, safe=False)

    @staticmethod
    def other(data):
        result = {"status": 3002, "data": data}
        return JsonResponse(result,safe=False)
# 用户的响应
class UserResponse():
    @staticmethod
    def success(data):
        result = {"status": 4000, "data": data}
        return JsonResponse(result,safe=False)

    @staticmethod
    def failed(data):
        result = {"status": 4001, "data": data}
        return JsonResponse(result, safe=False)

    @staticmethod
    def other(data):
        result = {"status": 4002, "data": data}
        return JsonResponse(result,safe=False)


# 评论的响应全部是5开头的
class CommentResponse():
    @staticmethod
    def success(data):
        result = {"status": 5000, "data": data}
        return JsonResponse(result, safe=False)

    @staticmethod
    def failed(data):
        result = {"status": 5001, "data": data}
        return JsonResponse(result, safe=False)

    @staticmethod
    def other(data):
        result = {"status": 5002, "data": data}
        return JsonResponse(result, safe=False)
# 订单的响应全部是6开头的
class OrderResponse():
    @staticmethod
    def success(data):
        result = {"status": 6000, "data": data}
        return JsonResponse(result, safe=False)

    @staticmethod
    def failed(data):
        result = {"status": 6001, "data": data}
        return JsonResponse(result, safe=False)

    @staticmethod
    def other(data):
        result = {"status": 6002, "data": data}
        return JsonResponse(result, safe=False)

# 地址响应是7
class AddressResponse():
    @staticmethod
    def success(data):
        result = {"status": 7000, "data": data}
        return JsonResponse(result, safe=False)

    @staticmethod
    def failed(data):
        result = {"status": 7001, "data": data}
        return JsonResponse(result, safe=False)

    @staticmethod
    def other(data):
        result = {"status": 7002, "data": data}
        return JsonResponse(result, safe=False)