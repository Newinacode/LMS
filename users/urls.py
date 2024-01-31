
from django.urls import path
from .views import UserViewSet
urlpatterns = [
    path('',UserViewSet.as_view({'get': 'list','post': 'create'})),
    path('<pk>/',UserViewSet.as_view({'post': 'update','delete':'destory','get':'retrieve'})),
]
