from django.shortcuts import render
from django.contrib.auth import logout, login, authenticate
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
# from django.contrib.auth.forms import UserCreationForm
from .forms import MyUserCreateForm as UserCreationForm
from PIL import Image
from django.conf import settings


# Create your views here.


def logout_view(request):
    """ 注销用户登录 """
    logout(request)
    return HttpResponseRedirect(reverse('blog:index'))


def register(request):
    """ 用户注册 """
    if request.method != 'POST':
        form = UserCreationForm()
    else:
        form = UserCreationForm(data=request.POST)

        if form.is_valid():
            new_user = form.save()
            authenticated_user = authenticate(
                username=new_user.username, password=request.POST['password1'])
            login(request, authenticated_user)
            return HttpResponseRedirect(reverse('blog:index'))
    context = {'form': form}
    return render(request, 'users/register.html', context)


def profile_setting(request):
    """ 用户账户设置 """
    if request.method != 'POST':
        fname = ''
    else:
        rquire_head_pic = request.FILES['head_pic']
        fname = '%s/pic/%s' % (settings.MEDIA_ROOT, rquire_head_pic)
        with open(fname, 'wb') as pic:
            for c in rquire_head_pic.chunks():
                pic.write(c)
        fname = '/media' + fname.split('media')[1]
        author = request.user
        author.head_portrait = fname
        author.save()

    context = {'pic': fname}
    return render(request, 'users/profile_setting.html', context)
