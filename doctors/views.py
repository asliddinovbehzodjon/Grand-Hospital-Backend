from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
# Create your views here.
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
from rest_framework.viewsets import ModelViewSet
from .models import Doctor
from .serializer import DoctorSerializer
class DoctorViewset(ModelViewSet):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer
    pagination_class = CustomeBasicPagination
def error_404(request,exception):
    return render(request,'error.html')