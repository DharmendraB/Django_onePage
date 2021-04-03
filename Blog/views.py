from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def blog(request):
    # return render(request,'onepage/home.html')
    return render(request,'Blog/blog.html')
    
def blogSingle(request):
    # return render(request,'onepage/home.html')
    return render(request,'Blog/blog-single.html')
