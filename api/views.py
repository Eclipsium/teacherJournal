
# Create your views here.
from django.shortcuts import render
from rest_framework import viewsets

from api.models import *
from api.serializers import StudentSerializer


class StudentsViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


def index(request):
    return render(request, 'index.html')

