from django.shortcuts import render
from .models import SampleModel

def app1_view(request):
    data = SampleModel.objects.first()
    return render(request, "interface.html", {"data": data})