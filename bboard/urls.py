from django.urls import path
from bboard.views import index, zero_page, main

urlpatterns = [
    path('main/', main),
    path('', zero_page),
    path('index', index),
]
