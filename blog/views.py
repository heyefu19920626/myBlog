from django.shortcuts import render
from urllib.parse import unquote
from django.http import HttpResponseRedirect, Http404, HttpResponse
from django.utils.translation import LANGUAGE_SESSION_KEY
from django.utils.http import is_safe_url
from .models import Article
import markdown

# Create your views here.


def index(request):
    """ 定位到首页 """
    articles = Article.objects.all().order_by('-created_time')
    context = {'articles': articles}
    return render(request, 'blog/index.html', context)


def article_details(request, article_id):
    """ 去往文章详情页,接收参数文章id """
    article_info = Article.objects.get(id=article_id)
    article = {}
    article['title'] = article_info.title
    article['body'] = markdown.markdown(article_info.body, extensions=[
                                       'markdown.extensions.extra', 'markdown.extensions.codehilite', 'markdown.extensions.toc', ])
    context = {'article': article}
    return render(request, 'blog/article_details.html', context)


def change_language(request, language):
    """ 切换语言并重定向到之前的页面 """
    lang_code = language
    if hasattr(request, 'session'):
        request.session[LANGUAGE_SESSION_KEY] = lang_code
    else:
        response.set_cookie(
            settings.LANGUAGE_COOKIE_NAME, lang_code,
            max_age=settings.LANGUAGE_COOKIE_AGE,
            path=settings.LANGUAGE_COOKIE_PATH,
            domain=settings.LANGUAGE_COOKIE_DOMAIN,
        )
    next = request.POST.get('next', request.GET.get('next'))
    if ((next or not request.is_ajax()) and
            not is_safe_url(url=next, allowed_hosts={request.get_host()}, require_https=request.is_secure())):
        next = request.META.get('HTTP_REFERER')
        if next:
            next = unquote(next)  # HTTP_REFERER may be encoded.
        if not is_safe_url(url=next, allowed_hosts={request.get_host()}, require_https=request.is_secure()):
            next = '/'
    response = HttpResponseRedirect(next) if next else HttpResponse(status=204)
    return response
