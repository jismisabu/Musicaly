from django.shortcuts import render

from django.contrib.auth.models import User
 
from rest_framework import viewsets

from rest_framework import status

from rest_framework.viewsets import ModelViewSet

from rest_framework.response import Response

from rest_framework.decorators import action

from rest_framework import authentication,permissions

from rest_framework.generics import RetrieveUpdateDestroyAPIView

from api import serializers

from api.serializers import AlbumSerializer, ReviewSerializer, TrackSerializer, UserSerializer

from api.models import Album, Tracks


class SignUpView(viewsets.ViewSet):


    def create(self,request,*args,**kwargs):

        serializer=UserSerializer(data=request.data)

        if serializer.is_valid():

            serializer.save()

            return Response(data=serializer.data)
        
        else:

             return Response(data=serializer.errors)


class AlbumViewSetView(ModelViewSet):

    serializer_class = AlbumSerializer

    queryset = Album.objects.all()


    @action(methods=["post"],detail=True)
    def add_track(self,request,*args,**kwargs):

        id=kwargs.get("pk")

        album_instance = Album.objects.get(id=id)

        serializer = TrackSerializer(data=request.data)

        if serializer.is_valid():

            serializer.save(album=album_instance)

            return Response(data=serializer.data)
        
        else:

            return Response(data=serializer.errors)
        

    @action(methods=["post"],detail=True)
    def add_review(self,request,*args,**kwargs):

        id=kwargs.get("pk")

        album_instance = Album.objects.get(id=id)

        serializer = ReviewSerializer(data=request.data)

        if serializer.is_valid():

            serializer.save(album=album_instance)

            return Response(data=serializer.data)
        
        else:

            return Response(data=serializer.errors)
        


class TrackMixinView(RetrieveUpdateDestroyAPIView):

    serializer_class = TrackSerializer

    queryset = Tracks.objects.all()

    








