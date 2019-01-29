from django.http import Http404
from django.shortcuts import render, get_object_or_404
#from django.http import HttpResponse
from .models import Album, Song
# Create your views here.

def index(request):
    all_albums = Album.objects.all()
    return render(request, 'music/index.html', {'all_albums':all_albums})

def detail(request, album_id):
    #album = Album.objects.get(pk=album_id)
    album = get_object_or_404(Album, pk=album_id)
    return render(request, 'music/detail.html', {'album':album})

def favorite(request, album_id):
    album = get_object_or_404(Album, pk=album_id)
    try:
        seleted_song = album.song_set.get(pk=request.POST['song'])
    except (KeyError, Song.DoesNotExist):
        return render(request, 'music/detail.html', {'album':album, 'error_message':"You didnt select a valid song"} )
    else:
        seleted_song.is_favorite=True
        seleted_song.save()
        return render(request, 'music/detail.html', {'album': album})

