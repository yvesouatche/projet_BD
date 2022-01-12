from django.urls import path
from .import views
urlpatterns = [
path("",views.home,name="home")
#path('article_list', views.article_list, name='article-list'),
    ]
