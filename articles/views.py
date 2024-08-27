from typing import Any
from django.db.models.query import QuerySet
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView

from datetime import datetime

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

        context["archives"] = self.get_previous_month()
        context["categories"] = Article.CATEGORIES

        return context
    
    
    def get_queryset(self):
        articles = Article.objects.filter(status='PUBLISHED').order_by("-published")

        year = self.kwargs.get('year', None)
        month = self.kwargs.get('month', None)
        
        print("year", year, "month", month)
        
        if year and month:
            print('dentro if')
            return articles.filter(published__year=year, published__month=month)
        
        tag = self.kwargs.get('category_tag', None)
        if tag:
            return articles.filter(category__in=[tag])
        
        return articles
    
    
    def get_previous_month(self):
        previous_months = []

        for i in range(12):
            month = datetime.now().month - i
            year = datetime.now().year

            if month <= 0:
                month += 12
                year -= 1
            previous_months.append(
                {"month": month, "year": year, "date": datetime(year, month, 1)}
            )

        return previous_months