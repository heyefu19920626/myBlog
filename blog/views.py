from django.shortcuts import render

# Create your views here.

def index(request):
    """ 定位到首页 """
    return render(request, 'blog/index.html')