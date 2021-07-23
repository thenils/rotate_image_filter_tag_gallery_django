from django.urls import path
from .views import ImageListView, ImageView, AddImage, rotateLeft, rotateRight

urlpatterns = [
    path('', ImageListView, name='imagelistview'),
    path('image/<int:ImageID>/', ImageView, name='image'),
    path('add/', AddImage, name='add'),
    path('rotateleft/<int:ImageID>/', rotateLeft, name='rotateLeft'),
    path('rotateright/<int:ImageID>/', rotateRight, name='rotateRight')
]
