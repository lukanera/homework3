from django.shortcuts import render, redirect
from .models import Article
from .form import ArticleForm

def create_article(request):
    articlefrom = ArticleForm
    if request.method == 'GET':
        articlefrom = ArticleForm(request.GET) 
        if articlefrom.is_valid(): 
            articlefrom.save() 
            return redirect('create_article') 
    
    
    articles = Article.objects.all()
    context = {'articles': articles,
               'form': articlefrom}

    return render(request, 'create_article.html', context=context)  

def show_articles(request):
    articles = Article.objects.all()
    context = {'articles': articles}
    return render(request, 'show_articles.html', context=context)