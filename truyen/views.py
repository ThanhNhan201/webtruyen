from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status, generics, viewsets
from rest_framework.views import APIView
from rest_framework import serializers
from .models import Truyen, Comment
from .serializers import TruyenSerializer, TruyenDetailSerializer, CommentSerializer


# Create your views here.

class TruyenApiView(generics.ListCreateAPIView):
    queryset = Truyen.objects.filter(removed=False)
    serializer_class = TruyenSerializer

    def get(self, request):
        obj = Truyen.objects.filter(removed=False)
        serializer = TruyenSerializer(obj, many=True)
        return Response(serializer.data, status=200)

    def post(self, request):

        serializer = TruyenSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request):
        truyen = Truyen.objects.all()
        for obj in truyen:
            obj.removed = True
            serializer = TruyenSerializer(data=obj)
            if serializer.is_valid():
                serializer.save()
            obj.save()
        return Response({'msg': 'all deleted'}, status=status.HTTP_204_NO_CONTENT)


class TruyenDetailView(APIView):
    def get(self, request, id):
        try:
            obj = Truyen.objects.get(id=id)
            if (obj.removed == True):
                msg = {"msg": "be removed"}
                return Response(msg)
        except Truyen.DoesNotExist:
            msg = {"msg": "not found"}
            return Response(msg, status=status.HTTP_400_BAD_REQUEST)
        obj.views = obj.views + 1
        obj.save()
        serializer = TruyenDetailSerializer(obj)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, id):
        try:
            obj = Truyen.objects.get(id=id)
            if (obj.removed == True):
                msg = {"msg": "be removed"}
                return Response(msg)
        except Truyen.DoesNotExist:
            msg = {"msg": "not found"}
            return Response(msg, status=status.HTTP_400_BAD_REQUEST)
        serializer = TruyenDetailSerializer(obj, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_205_RESET_CONTENT)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        try:
            obj = Truyen.objects.get(id=id)
            if (obj.removed == True):
                msg = {"msg": "be removed"}
                return Response(msg)
        except Truyen.DoesNotExist:
            msg = {"msg": "not found"}
            return Response(msg, status=status.HTTP_400_BAD_REQUEST)
        obj.removed = True
        serializer = TruyenDetailSerializer(data=obj)
        if serializer.is_valid():
            serializer.save()
        obj.save()
        return Response({'msg': 'deleted'}, status=status.HTTP_204_NO_CONTENT)

class ViewSortAPI(APIView):
    def get(self, request):
        obj = Truyen.objects.filter(removed=False).order_by('views')[:10]
        serializer = TruyenDetailSerializer(obj, many=True)
        return Response(serializer.data, status=200)

class DateSortAPI(APIView):
    def get(self, request):
        obj = Truyen.objects.filter(removed=False).order_by('updated_at')[:10]
        serializer = TruyenDetailSerializer(obj, many=True)
        return Response(serializer.data, status=200)


class CommentAPI(APIView):
    # queryset = Comment.objects.all().order_by('-created_at')
    # serializer_class = CommentSerializer
    def get(self, request, id):
        user = request.user
        comments = Comment.objects.filter(truyen=id, removed=False).order_by('-created_at')
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data, status=200)

    def post(self, request, id):
        user = request.user
        truyen = Truyen.objects.get(id=id)
        # if request.user.is_authenticated:
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            truyen.number_of_comment = truyen.number_of_comment + 1
            truyen.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)
        # return Response({'msg': 'user not authenticated'})

    def delete (self, request, id):
        try:
            obj = Comment.objects.get(id=id)
            if(obj.removed == True):
                msg = {"msg": "be removed"}
                return Response(msg)
        except Comment.DoesNotExist:
            msg = {"msg": "not found"}
            return Response(msg, status=status.HTTP_400_BAD_REQUEST)
        obj.removed = True
        serializer = CommentSerializer(data=obj)
        if serializer.is_valid():
            serializer.save()
        obj.save()
        return Response({'msg': 'deleted'}, status=status.HTTP_204_NO_CONTENT)

    def put(self, request, id):
        try:
            obj = Comment.objects.get(id=id)
            if (obj.removed == True):
                msg = {"msg": "be removed"}
                return Response(msg)
        except Comment.DoesNotExist:
            msg = {"msg": "not found"}
            return Response(msg, status=status.HTTP_400_BAD_REQUEST)
        serializer = CommentSerializer(obj, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_205_RESET_CONTENT)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




