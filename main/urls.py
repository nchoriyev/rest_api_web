from django.urls import path
from .views import HomeView, AlbomView, ArtistView, SongView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('artist/', ArtistView.as_view(), name='artist'),
    path('albom/', AlbomView.as_view(), name='albom'),
    path('song/', SongView.as_view(), name='song'),
]
