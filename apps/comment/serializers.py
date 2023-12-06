from rest_framework import serializers

from apps.address.models import UserAddress
from apps.comment.models import Comment
from apps.goods.models import Goods
from apps.order.models import OrderGoods
from muxi_shop_api2.settings import IMAGE_URL


class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = ('__all__')