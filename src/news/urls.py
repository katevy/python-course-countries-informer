"""
Доступные для вызова URLs
"""
from django.urls import path

from news.views import get_news

urlpatterns = [
    path("news/<str:alpha2code><str:page>", get_news, name="news"),
]
