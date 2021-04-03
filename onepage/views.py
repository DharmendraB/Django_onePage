from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
# def index(request):
#     return HttpResponse('Index Function Call')

def index(request):
    # return render(request,'onepage/home.html')
    return render(request,'onepage/index.html')
def blog(request):
    # return render(request,'onepage/home.html')
    return render(request,'onepage/blog.html')
def blogSingle(request):
    # return render(request,'onepage/home.html')
    return render(request,'onepage/blog-single.html')
    
def PortfolioDetails(request):    
    return render(request,'onepage/portfolio-details.html')
