"""
URL configuration for API
"""
from django.urls import path
from . import views

urlpatterns = [
    path('health/', views.health_check, name='health_check'),
    path('info/', views.api_info, name='api_info'),
    path('contributors/', views.list_contributors, name='list_contributors'),
    path('issues/', views.list_issues, name='list_issues'),
    path('stats/', views.stats, name='stats'),
]
