from django.shortcuts import render
from django.views import View
import requests

class HomeView(View):
    def get(self, request):
        artists = requests.get("http://localhost:8000/api/artists-web").json()
        context = {
            "artists":artists
        }
        return render(request, 'home.html', context)

class ArtistView(View):
    def get(self, request):
        artists = requests.get("http://localhost:8000/api/artists-web").json()
        context = {
            "artists": artists
        }
        return render(request, 'artist.html', context)

class AlbomView(View):
    def get(self, request):
        alboms = requests.get("http://localhost:8000/api/albom-web").json()
        context = {
            "alboms": alboms
        }
        return render(request, 'albom.html', context)

class SongView(View):
    def get(self, request):
        songs = requests.get("http://localhost:8000/api/song-web").json()
        context = {
            "songs": songs
        }
        return render(request, 'song.html', context)

