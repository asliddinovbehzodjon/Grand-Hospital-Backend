from django.shortcuts import render

# Create your views here.
from .models import Drug
from.serializer import DrugSerializer
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from django.db.models import  Q
from rest_framework.views import APIView
from rest_framework import  status
from rest_framework.pagination import PageNumberPagination
from rest_framework.viewsets import ModelViewSet
class CustomeBasicPagination(PageNumberPagination):
    page_size = 6

    def get_paginated_response(self, data):
        return Response({

            'next': self.get_next_link(),
            'previous': self.get_previous_link(),
            'current_page_num': self.page.number,
            'current_page_num_size': self.page.paginator.per_page,
            'all_pages': self.page.paginator.num_pages,
            'count': self.page.paginator.count,
            'results': data
        })
class DrugViewset(ModelViewSet):
    queryset = Drug.objects.all()
    serializer_class = DrugSerializer
    pagination_class = CustomeBasicPagination
class BasicPagination(PageNumberPagination):
    page_size = 6

    def get_paginated_response(self, data):
        return Response({

            'next': self.get_next_link(),
            'previous': self.get_previous_link(),
            'current_page_num': self.page.number,
            'all_pages': self.page.paginator.num_pages,
            'count': self.page.paginator.count,

            'results': data
        })
from doctors.pagination import PaginationHandlerMixin
class SearchDrug(APIView,PaginationHandlerMixin):
    pagination_class=BasicPagination
    def get(self,request,key):
        mydata = Drug.objects.filter(Q(title__icontains=key) | Q(description__icontains=key))
        page = self.paginate_queryset(mydata)
        if page is not None:
            serializer = self.get_paginated_response(DrugSerializer(page,
                                                                    many=True).data)
        else:
            serializer =DrugSerializer(mydata, many=True)

        return Response(serializer.data,status=status.HTTP_200_OK)
