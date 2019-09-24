from django.urls import path
from .views import home,album

app_name = 'diaries'

urlpatterns = [
    path('home/album/',album,name="album"),
    path('home/album/<slug:slug_category>',album,name='album'),
    path('home/',home,name='home'),
]