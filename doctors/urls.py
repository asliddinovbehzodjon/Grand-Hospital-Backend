from rest_framework.routers import DefaultRouter
from .views import DoctorViewset
from django.urls import path,include
router = DefaultRouter()
router.register('doctors',DoctorViewset)
urlpatterns = [
    path('',include(router.urls))
]
