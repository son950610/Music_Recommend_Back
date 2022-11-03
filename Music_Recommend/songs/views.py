from django.shortcuts import render
from rest_framework.views import APIView
from .models import Song
# Create your views here.


class SearchView(APIView):
    def get(self, request):
        post_result = Song.object.all()
    pass
