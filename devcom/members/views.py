from django.shortcuts import render
from django.http import HttpResponse
from django.core import serializers
from .models import memberList

# We use serializers to convert querySets to JSON format

# Create your views here.
def displayMembers(request):
    queryset = memberList.objects.all()
    data = serializers.serialize('json', queryset)
    return HttpResponse(data ,content_type='application/json')
