from django.urls import path
from .views import post_list

urlpatterns = [
    path('items/', post_list),
]
