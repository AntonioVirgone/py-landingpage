from django.urls import path
from .views import ArticleDetailView, ArticleListView

app_name = "articles"

urlpatterns = [
    path('list/<slug:category_tag>/', ArticleListView.as_view(), name='article-list'),
    path('list/archives/<slug:year>/<slug:month>/', ArticleListView.as_view(), name='article-archive'),
    path('<slug:slug>/', ArticleDetailView.as_view(), name='article-detail'),
]
