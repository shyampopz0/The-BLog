from django.urls import path
from .views import *


urlpatterns = [
    path('',HomeView.as_view(),name="home"),
    path('drafts/list/',DraftView.as_view(),name="draft"),
    path('articleDetails/<slug:slug>/',articleDetailView.as_view(),name="article-detail"),
    path('addBlog/',addArticleView.as_view(),name="addBlog"),
    path('addCategory/',addCategoryView.as_view(),name="addCategory"),
    path('Category/List/',categoryListView.as_view(),name="categoryListView"),
    path('Category/<slug:slug>/',categoryView,name="categoryList"),
    path('article/edit/<slug:slug>/',updateArticleView.as_view(),name="update-Blog"),
    path('article/remove/<slug:slug>/',deleteArticleView.as_view(),name="delete-Blog"),
    path('tags/<slug:slug>/',TagIndexView.as_view(),name="tagged"),
    path('tagslist/', TagListView.as_view(), name="tag"),
    path('about/', aboutView, name="aboutme")
]

# path('Category/<str:cats>/',categoryView,name="categoryList"),
#path('articleDetails/<slug:slug>,<int:pk>/', articleDetailView.as_view(), name="article-detail"),