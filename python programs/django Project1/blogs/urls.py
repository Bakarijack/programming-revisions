from django.urls import path
from . import views

urlpatterns = [
    path('bloglist/', views.blog),
    path('blognumber/', views.htmlBlog)
]
