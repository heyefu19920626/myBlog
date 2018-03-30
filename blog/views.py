from django.shortcuts import render
from urllib.parse import unquote
from django.http import HttpResponseRedirect, Http404, HttpResponse
from django.utils.translation import LANGUAGE_SESSION_KEY
from django.utils.http import is_safe_url
from django.urls import reverse
from .models import Article, Category
import markdown
#from markdown.extensions import Extension
from .forms import ArticleForm
from django.contrib.auth.models import User

# Create your views here.


def index(request):
    """ 定位到首页 """
    articles = Article.objects.all().order_by('-created_time')
    context = {'articles': articles}
    return render(request, 'blog/index.html', context)


def article_details(request, article_id):
    """ 去往文章详情页,接收参数文章id """
    article = Article.objects.get(id=article_id)
    # 获取文章作者
    author = article.author
    # 获取该作者的其他文章
    articles = get_articles_byauthor(author)
    article.body = markdown.markdown(article.body, extensions=[
        'markdown.extensions.extra',
        'markdown.extensions.codehilite',
        'markdown.extensions.toc',
        'markdown.extensions.fenced_code', ])
    context = {'article': article, "articles": articles, }
    return render(request, 'blog/article_details.html', context)



def get_articles_byauthor(article_author):
    """ 根据文章作者获取其所有文章 """
    articles = Article.objects.filter(author=article_author)
    return articles





def edit_article(request, article_id):
    """ 编辑文章 """
    article = Article.objects.get(id=article_id)

    if request.method != 'POST':
        form = ArticleForm(instance=article)
    else:
        print(request.POST['category'])
        form = ArticleForm(instance=article, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('blog:article_details', args=[article_id]))
        else:
            print('表单验证出错')
    categorys = Category.objects.all()
    context = {'article': article, 'form':form, 'categorys': categorys}
    return render(request, 'blog/edit_article.html', context)



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
