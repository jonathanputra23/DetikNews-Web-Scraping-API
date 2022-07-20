"""webScrape URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from turtle import title
from django.contrib import admin
from django.urls import path
from webScrape import views

from rest_framework.urlpatterns import format_suffix_patterns

from rest_framework.schemas import get_schema_view
from django.views.generic import TemplateView

urlpatterns = [
    path('scrape/', views.scrapeWebsite),
    path('getUrl/', views.getURL),
    path('openapi', get_schema_view(
        title="Detik News Scrape API",
        description="API for Scraping DetikNews"
    ), name='openapi-schema'),
    path('swagger-ui/', TemplateView.as_view(
            template_name='swagger-ui.html',
            extra_context={'schema_url':'openapi-schema'}
        ), name='swagger-ui')
    ]

urlpatterns = format_suffix_patterns(urlpatterns)