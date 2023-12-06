import datetime

from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from apps.user.models import User
from utils.password_encode import get_md5


class UserSerializers(serializers.ModelSerializer):
    #email作为用户名进行登陆,这里需要做一个唯一性的验证
    email=serializers.EmailField(required=True,allow_blank=False,
                                 validators=[UniqueValidator(queryset=User.objects.all(),message="该用户已经存在了")])
    password = serializers.CharField()
    birthday = serializers.DateTimeField("%Y -%m -%d %H:%M:%S")
    create_time = serializers.DateTimeField("%Y -%m -%d %H:%M:%S",required=False)

    # create 方法会被自动调用 , 这里可以做一些数据的验证和数据存储之前的加工
    def create(self, validated_data):
        print("create方法被调用了")
        validated_data["password"]=get_md5(validated_data["password"])
        validated_data["create_time"] = datetime.datetime.now().strftime("%Y -%m -%d %H:%M:%S")
        result=User.objects.create(**validated_data)
        return  result

    class Meta:
        model=User
        fields="__all__"