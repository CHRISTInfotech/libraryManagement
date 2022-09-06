from django.shortcuts import render

# Create your views here.


def head(request):
    return render(request, 'head.html')
