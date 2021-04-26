from django.http import Http404
from django.shortcuts import render
from .models import PageFeatures
from .serializers import YoutubeSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


# Create your views here.

class PageList(APIView):

    def get_object(self, pk):
        try:
            return PageFeatures.objects.get(pk=pk)
        except PageFeatures.DoesNotExist:
            raise Http404

    def get(self, request):
        list = PageFeatures.objects.all()
        serializer = YoutubeSerializer(list, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = YoutubeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)