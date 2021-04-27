from django.http import HttpResponse
from django.shortcuts import render


def homePage(request):
    return HttpResponse('home')
    # return render(request, 'HomePage.html')