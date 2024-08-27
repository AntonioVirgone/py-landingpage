from typing import Any
from django.db.models.query import QuerySet
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from .models import Article


# Create your views here.
class ArticleDetailView(DetailView):
    model = Article
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
    
    
class ArticleListView(ListView):
    model = Article
    # questa property consente di fare la paginazione nella view in modo automatico
    paginate_by = 3
    
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)        
        return context
    
    
    def get_queryset(self):
        articles = Article.objects.all().order_by("-published")

        year = self.request.GET.get('year')
        month = self.request.GET.get('month')
        
        if year != None and month != None:
            return articles.filter(published__year=year, published__month=month)
            
        return articles