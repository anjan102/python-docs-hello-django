from django.http import HttpResponse
from django.shortcuts import render

def hello(request):
    return HttpResponse("********** -( Hi HPE Team good evening, My Name is 'Bipin', I am learning AZURE Cloud Computing[AZ900] ) **************** ")
