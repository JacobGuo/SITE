from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse,HttpResponseNotFound
from .models import Article
# Create your views here.

def index(request):
	objects = Article.objects.all();
	return render(request,'Blog/index.html',{'article_list':objects})

def singlePage(request,pageID):
	blog = get_object_or_404(Article,pk=pageID)
	return render(request,'Blog/blog.html',{'blog':blog})
	
