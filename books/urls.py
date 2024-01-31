
from django.urls import path
from .views import BookViewSet
urlpatterns = [
    path('',BookViewSet.as_view({'get': 'list','post': 'create'})),
    path('<int:pk>/',BookViewSet.as_view({'post': 'update','delete':'destory','get':'retrieve'})),
    path('borrowed/',BookViewSet.as_view({'post': 'borrow'})),
    path('return/',BookViewSet.as_view({'post': 'return_book'})),
]
