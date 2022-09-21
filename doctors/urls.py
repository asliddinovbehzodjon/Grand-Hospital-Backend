from rest_framework.routers import DefaultRouter
from .views import DoctorViewset,Search
from django.urls import path,include
router = DefaultRouter()
router.register('doctors',DoctorViewset)
urlpatterns = [
    path('',include(router.urls)),
    path('search/<str:key>/',Search.as_view())
]
