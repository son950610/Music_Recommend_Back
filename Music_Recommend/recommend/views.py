from django.shortcuts import get_list_or_404
from rest_framework import status 
from rest_framework.response import Response
from rest_framework.views import APIView
from recommend.recom import get_recommendations
import random

from songs.models import Song
from recommend.serializers import (
    SongListSerializer,
    )


class SongListView(APIView):
    def get(self, request, format=None):
        song_list = get_list_or_404(Song)
        listserializer = SongListSerializer([random.choice(song_list) for i in range(12)], many=True)
        return Response(listserializer.data, status=status.HTTP_200_OK)