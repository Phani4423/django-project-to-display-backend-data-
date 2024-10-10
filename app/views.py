from django.shortcuts import render

# Create your views here.
def fun(request):
    d = {'name':'phsni','number':[1234,5678]}
    return render(request,'loop.html',d)

