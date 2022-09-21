from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from django.db.models import Q
from rest_framework import status
# Create your views here.
class CustomeBasicPagination(PageNumberPagination):
    page_size = 8

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
from rest_framework.viewsets import ModelViewSet
from .models import Doctor
from .serializer import DoctorSerializer
from rest_framework.views import APIView
class DoctorViewset(ModelViewSet):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer
    pagination_class = CustomeBasicPagination
def error_404(request,exception):
    return render(request,'error.html')


class BasicPagination(PageNumberPagination):
    page_size = 4

    def get_paginated_response(self, data):
        return Response({

            'next': self.get_next_link(),
            'previous': self.get_previous_link(),
            'current_page_num': self.page.number,
            'all_pages': self.page.paginator.num_pages,
            'count': self.page.paginator.count,

            'results': data
        })
from .pagination import PaginationHandlerMixin
class Search(APIView,PaginationHandlerMixin):
    pagination_class=BasicPagination
    def get(self,request,key):
        mydata = Doctor.objects.filter(Q(fullname__icontains=key) | Q(profession__icontains=key))
        page = self.paginate_queryset(mydata)
        if page is not None:
            serializer = self.get_paginated_response(DoctorSerializer(page,
                                                                    many=True).data)
        else:
            serializer =DoctorSerializer(mydata, many=True)

        return Response(serializer.data,status=status.HTTP_200_OK)
