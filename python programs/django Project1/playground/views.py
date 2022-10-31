from django.shortcuts import render
from django.http import HttpResponse
import math

# Create your views here.
#request handler
def say_hello(request):
    return render(request, 'hello.html', {'name': 'Bakari'})

def calculate(request):
    number1 = 45
    number2 = 5
    return HttpResponse(math.pow(number1,number2))
