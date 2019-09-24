from django.shortcuts import render
from .models import Category,AlbumImage,Album

# Create your views here.
def home(request):
    template = "diaries/home.html"
    context = {}
    return render(request,template,context)


def album(request,slug_category=None):

    print("slug - > ",slug_category)

    category = Category.objects.all()
    albums = Album.objects.filter(show=True)


    if slug_category:
        cat = Category.objects.get(name=slug_category)
        albums = albums.filter(category=cat)
        print("inside album --> ",albums)
    print("outside album -->",albums)

    template = "diaries/album.html"
    context = {'category':category,'albums':albums}

    return render(request,template,context)