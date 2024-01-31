
from django.urls import path
from .views import BookViewSet
urlpatterns = [
    path('books/',BookViewSet.as_view({'get': 'list'})),
    path('books/create',BookViewSet.as_view({'post': 'create'})),
    path('books/<pk>',BookViewSet.as_view({'post': 'update','delete':'destory','get':'retrieve'})),
]
