from django.urls import path
from .views import *

urlpatterns = [
    path('', news_home, name = 'news_home'),
    path('create', create, name='create'),
    path('<int:pk>', ArticleDetailView.as_view(), name='news_detail'),
    path('<int:pk>/update', ArticleUpdateView.as_view(), name='news_update'),
    path('<int:pk>/delete', ArticleDeleteView.as_view(), name='news_delete')
]