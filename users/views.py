from django.shortcuts import render
from django.contrib.auth.views import logout
from django.http import HttpResponseRedirect
from django.urls import reverse


# Create your views here.


def logout_view(request):
    """ 注销用户登录 """
    logout(request)
    return HttpResponseRedirect(reverse('blog:index'))
