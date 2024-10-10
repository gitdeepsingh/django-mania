from django.shortcuts import render
from django.http import HttpResponse

# Create your requets here.

def say_hello(request):
    # return HttpResponse("Hello World!")
    return render(request, 'hello.html', {'name': 'Deep Singh'})


 