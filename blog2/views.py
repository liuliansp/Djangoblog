from django.shortcuts import render
from django.http import HttpResponse
from . import  models
def index(request):
    student=models.students.objects.get(pk=1)
    return render(request, 'blog2/index.html', {'hello':student})
# Create your views here.
