from django.urls import path
from .views import ArticleDetailView, ArticleListView

urlpatterns = [
    path('list/', ArticleListView.as_view(), name='article-list'),
    path('<slug:slug>/', ArticleDetailView.as_view(), name='article-detail'),
]
