from rest_framework import serializers

from apps.goods.models import Goods
from apps.order.models import OrderGoods, Order
from muxi_shop_api2.settings import IMAGE_URL


class OrderGoodsSerializer(serializers.ModelSerializer):

    class Meta:
        model = OrderGoods
        fields = ('__all__')
class OrderSerializer(serializers.ModelSerializer):

    class Meta:
        model = Order
        fields = ('__all__')
class OrderManyGoodsSerializer(serializers.Serializer):
    trade_no = serializers.CharField()
    email = serializers.CharField()
    order_amount = serializers.DecimalField(max_digits=10, decimal_places=2)
    address_id = serializers.IntegerField()
    pay_status = serializers.CharField(max_length=155)
    pay_time = serializers.DateTimeField()
    ali_trade_no = serializers.CharField(max_length=255)
    is_delete = serializers.IntegerField()
    create_time = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")
    order_info=serializers.SerializerMethodField()

    def get_order_info(self,obj):
        # ser=GoodsSerializer(Goods.objects.filter(sku_id=obj.sku_id).first(),many=False).data
        ser=OrderGoodsSerializer(OrderGoods.objects.filter(trade_no=obj.trade_no).all(),many=True).data
        for i in ser:
            goods_data=Goods.objects.filter(sku_id=i.get("sku_id")).first()
            i["p_price"]=goods_data.p_price
            i["image"]=IMAGE_URL+goods_data.image
            i["name"]=goods_data.name
            i["shop_name"]=goods_data.shop_name
        return ser