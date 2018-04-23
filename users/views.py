from django.shortcuts import render
from django.contrib.auth import logout, login, authenticate
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
# from django.contrib.auth.forms import UserCreationForm
from .forms import MyUserCreateForm as UserCreationForm
from django.conf import settings
import os
from django.http import JsonResponse


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


def head_pic_setting(request):
    """ 用户头像 """
    if request.method != 'POST':
        fname = ''
    else:
        rquire_head_pic = request.FILES['head_pic']
        # 将上传的图片重命名
        pic_name = rquire_head_pic.name
        print(pic_name)
        suffix = pic_name[pic_name.rindex('.'):]
        pic_name = str(request.user.id) + '_head' + suffix
        # 将上传的图片写入文件
        fname = '%s/pic/head/%s' % (settings.MEDIA_ROOT, pic_name)
        with open(fname, 'wb') as pic:
            for c in rquire_head_pic.chunks():
                pic.write(c)

        # 返回图片路径
        fname = settings.MEDIA_URL + 'pic/head/' + pic_name
        print(fname)
        # 将头像路径保存入数据库
        author = request.user
        author.head_portrait = fname
        author.save()

    context = {'pic': fname}
    return render(request, 'users/setting.html', context)


def upload_head_pic(request):
    """ 上传用户头像 """
    rquire_head_pic = request.FILES['head_pic']
    # 将上传的图片重命名
    pic_name = rquire_head_pic.name
    suffix = pic_name[pic_name.rindex('.'):]
    pic_name = str(request.user.id) + '_head_temp' + suffix
    # 将上传的图片写入文件
    fname = '%s/pic/head/%s' % (settings.MEDIA_ROOT, pic_name)
    with open(fname, 'wb') as pic:
        for c in rquire_head_pic.chunks():
            pic.write(c)

    # 返回图片路径
    fname = settings.MEDIA_URL + 'pic/head/' + pic_name
    return HttpResponse(fname)


def upload_person_info(request):
    """ 修改用户公开个人信息 """

    # 获取相关信息
    nick_name = request.POST['nick_name']
    sex = request.POST['sex']
    bio = request.POST['bio']
    head_pic_path = request.POST['pic_path']

    if head_pic_path == None or head_pic_path == '':
        context = {'error': '没有图片'}
        return JsonResponse(context)

    if  'head_temp' not in head_pic_path: 
        author = request.user
        author.nick_name = nick_name
        author.sex = sex
        author.bio = bio
        author.save()
        context = {'error' : '没有临时图片'}
        return JsonResponse(context)

    head_pic_path = head_pic_path.split('media')[-1]
    # 获取图片绝对路径
    head_pic_path = '%s%s' % (settings.MEDIA_ROOT, head_pic_path)

    if os.path.exists(head_pic_path):
        # 头像保存路径
        new_name = head_pic_path.replace('head_temp', 'head')
        if os.path.exists(new_name):
            # 删除已有头像
            os.remove(new_name)
        # 重命名头像
        os.rename(head_pic_path, new_name)
    author = request.user
    # 将头像路径保存入数据库
    author = request.user
    # 返回头像新路径
    new_name = settings.MEDIA_URL + new_name.split(settings.MEDIA_ROOT)[-1]
    # 保存进数据库
    author.nick_name = nick_name
    author.sex = sex
    author.bio = bio
    author.head_portrait = new_name
    author.save()
    context = {'success': new_name}
    return JsonResponse(context)
