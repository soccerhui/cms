#coding:utf-8
from django.shortcuts import render
from django.http import HttpResponse
from news.models import Article, Column
from django.shortcuts import redirect

# Create your views here.

def index(request):
    columns = Column.objects.all()
    return render(request, 'index.html', {'columns':columns}) 
def column_detail(request, column_slug):
    column = Column.objects.get(slug=column_slug)
    return render(request, 'news/column.html',  {'column': column})

def article_detail(request, pk, article_slug):
    article = Article.objects.get(pk=pk)

    if article_slug != article.slug:
        return redirect(article, permanet=True)

    return render(request, 'news/article.html', {'article': article})
