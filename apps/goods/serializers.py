from rest_framework import serializers

from apps.goods.models import Goods
from muxi_shop_api2.settings import IMAGE_URL


class GoodsSerializer(serializers.ModelSerializer):
    #这里写的字段就是想要进行序列化处理的字段
    image=serializers.SerializerMethodField()
    create_time=serializers.DateTimeField("%Y -%m -%d %H:%M:%S")
    def get_image(self,obj):
        new_image_path = IMAGE_URL +obj.image
        return new_image_path
    class Meta:
        model = Goods
        fields = ('__all__')