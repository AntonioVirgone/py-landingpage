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
    