from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def formatList(l):
    for item in l:
        return item

def blog(request):
    list1 = [1,2,3,4,5,6]
    return HttpResponse(list1)

def htmlBlog(request):
    return render(request,'first_blog.html', {'app':'Blog Web App'})