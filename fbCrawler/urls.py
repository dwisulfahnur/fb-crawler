"""fbCrawler URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from comments.views import get_post_commments_api, crawl_post_comments_api

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/comments/<str:post_id>', get_post_commments_api),
    path('api/comments/<str:pid>_<str:post_id>/crawl', crawl_post_comments_api),
]
