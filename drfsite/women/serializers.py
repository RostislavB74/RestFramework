from rest_framework import serializers
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from .models import Women
import io


# class WomenModel:
#     def __init__(self, title, content):
#         self.title = title
#         self.content = content


class WomenSerializer(serializers.ModelSerializer):
    user= serializers.HiddenField(default=serializers.CurrentUserDefault())
    class Meta:
        model = Women
        fields = '__all__'

