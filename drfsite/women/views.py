from django.shortcuts import render
from django.forms.models import model_to_dict
from rest_framework import generics
from .models import Women
from .serializers import WomenSerializer
from rest_framework.views import APIView, Response
from rest_framework.decorators import action
# Create your views here.


class WomenAPIView(APIView):
    def get(self, request):
        w = Women.objects.all()
        return Response({'posts': WomenSerializer(w, many=True).data})

# class WomenAPIView(APIView):
#     def get(self, request):
#         w = Women.objects.all()
#         return Response({"posts": WomenSerializer(w, many=True).data})

    # def post(self, request):
    #     post_new = Women.objects.create(
    #         title=request.data['title'],
    #         content=request.data['content'],
    #         cat_id=request.data['cat_id'])
    #     return Response({'posts': WomenSerializer(post_new, many=True).data})

    def post(self, request):
        serializer = WomenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response({'post': serializer.data})

    def put(self, request, *args, **kwargs):
        pk = kwargs.get("pk", None)
        if not pk:
            return Response({"error": "Method PUT not allowed"})
        try:
            instance = Women.objects.get(pk=pk)
        except:
            return Response({"error": "Object does not exist"})
        serializer = WomenSerializer(data=request.data, instance=instance)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"post": serializer.data})
