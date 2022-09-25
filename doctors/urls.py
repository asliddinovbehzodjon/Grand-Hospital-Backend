from rest_framework.routers import DefaultRouter
from .views import DoctorViewset,Search
from drugs.views import DrugViewset,SearchDrug
from django.urls import path,include
router = DefaultRouter()
router.register('doctors',DoctorViewset),
router.register('drugs',DrugViewset)
urlpatterns = [
    path('',include(router.urls)),
    path('search/<str:key>/',Search.as_view()),
    path('searchdrug/<str:key>/',SearchDrug.as_view())
]
